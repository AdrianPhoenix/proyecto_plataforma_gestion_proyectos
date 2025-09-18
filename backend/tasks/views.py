from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCreateSerializer, TaskCommentSerializer
from projects.models import ProjectMember
from notifications.services import NotificationService

class TaskListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar y crear tareas.
    GET: Retorna tareas de proyectos donde el usuario es miembro
    POST: Crea nueva tarea y envía notificación si se asigna
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtra tareas de proyectos donde el usuario es miembro."""
        project_id = self.request.query_params.get('project')
        if project_id:
            # Filtrar por proyecto específico
            return Task.objects.filter(
                project_id=project_id,
                project__projectmember__user=self.request.user
            ).distinct()
        # Retornar todas las tareas de proyectos del usuario
        return Task.objects.filter(project__projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        """Retorna serializer apropiado según el método HTTP."""
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_create(self, serializer):
        """Crea tarea y envía notificación si se asigna a alguien."""
        task = serializer.save(created_by=self.request.user)
        # Notificar si se asigna la tarea a alguien
        if task.assigned_to:
            NotificationService.notify_task_assigned(task)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para operaciones CRUD en tarea específica.
    Solo miembros del proyecto pueden acceder.
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtra tareas de proyectos donde el usuario es miembro."""
        return Task.objects.filter(project__projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        """Retorna serializer apropiado según el método HTTP."""
        if self.request.method in ['PUT', 'PATCH']:
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_update(self, serializer):
        """Actualiza tarea y envía notificaciones según cambios."""
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
    """
    Agrega un comentario a una tarea.
    Solo miembros del proyecto pueden comentar.
    """
    try:
        # Verificar que la tarea existe y el usuario tiene acceso
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
    """
    Obtiene comentarios de una tarea específica.
    Solo miembros del proyecto pueden ver comentarios.
    """
    try:
        # Verificar acceso a la tarea
        task = Task.objects.get(id=task_id, project__projectmember__user=request.user)
        # Obtener comentarios ordenados por fecha
        comments = task.comments.all()
        serializer = TaskCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_tasks(request):
    """
    Retorna tareas asignadas al usuario autenticado.
    Usado en el dashboard para mostrar "Mis Tareas".
    """
    tasks = Task.objects.filter(assigned_to=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
