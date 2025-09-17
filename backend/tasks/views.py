from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCreateSerializer, TaskCommentSerializer
from projects.models import ProjectMember
from notifications.services import NotificationService

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
    
    def perform_create(self, serializer):
        task = serializer.save(created_by=self.request.user)
        # Notificar si se asigna la tarea a alguien
        if task.assigned_to:
            NotificationService.notify_task_assigned(task)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(project__projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_update(self, serializer):
        old_task = self.get_object()
        old_status = old_task.status
        old_assigned = old_task.assigned_to
        
        task = serializer.save()
        
        # Notificar si se completa la tarea
        if old_status != 'completed' and task.status == 'completed':
            NotificationService.notify_task_completed(task)
        
        # Notificar si se asigna a alguien nuevo
        if old_assigned != task.assigned_to and task.assigned_to:
            NotificationService.notify_task_assigned(task)

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
            comment = serializer.save()
            # Notificar sobre el nuevo comentario
            NotificationService.notify_comment_added(comment)
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
