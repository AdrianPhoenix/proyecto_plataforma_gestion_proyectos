from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCreateSerializer, TaskCommentSerializer
from projects.models import ProjectMember

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        if project_id:
            return Task.objects.filter(
                project_id=project_id,
                project__projectmember__user=self.request.user
            ).distinct()
        return Task.objects.filter(project__projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(project__projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskCreateSerializer
        return TaskSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task_comment(request, task_id):
    try:
        task = Task.objects.get(id=task_id, project__projectmember__user=request.user)
        serializer = TaskCommentSerializer(data=request.data, context={
            'request': request,
            'task': task
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_comments(request, task_id):
    try:
        task = Task.objects.get(id=task_id, project__projectmember__user=request.user)
        comments = task.comments.all()
        serializer = TaskCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
