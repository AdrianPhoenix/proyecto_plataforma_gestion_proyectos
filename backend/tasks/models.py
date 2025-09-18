from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
    """
    Modelo para gestión de tareas dentro de proyectos.
    Cada tarea pertenece a un proyecto y puede ser asignada a un usuario.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),       # Tarea pendiente
        ('in_progress', 'In Progress'), # Tarea en progreso
        ('completed', 'Completed'),   # Tarea completada
    ]
    
    # Información básica de la tarea
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField()
    
    # Relaciones
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tasks')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.project.name}"

class TaskComment(models.Model):
    """
    Modelo para comentarios en tareas.
    Permite a los usuarios colaborar y comunicarse sobre tareas específicas.
    """
    # Relaciones
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Contenido del comentario
    content = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Ordenar comentarios por fecha de creación (más recientes primero)
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.name}"
