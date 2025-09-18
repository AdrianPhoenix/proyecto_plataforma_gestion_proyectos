from django.db import models
from django.conf import settings

class Project(models.Model):
    """
    Modelo para gestión de proyectos.
    Cada proyecto puede tener múltiples miembros con diferentes roles.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),       # Proyecto pendiente de iniciar
        ('in_progress', 'In Progress'), # Proyecto en desarrollo
        ('completed', 'Completed'),   # Proyecto finalizado
        ('cancelled', 'Cancelled'),   # Proyecto cancelado
    ]
    
    # Información básica del proyecto
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Relaciones
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_projects')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ProjectMember', related_name='projects')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    """
    Modelo intermedio para la relación Many-to-Many entre Project y User.
    Define el rol específico de cada usuario en cada proyecto.
    """
    ROLE_CHOICES = [
        ('admin', 'Administrator'),    # Puede gestionar el proyecto y sus miembros
        ('collaborator', 'Collaborator'), # Puede crear y editar tareas
        ('viewer', 'Viewer'),         # Solo puede ver el proyecto
    ]
    
    # Relaciones
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Rol específico en este proyecto
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Un usuario solo puede tener un rol por proyecto
        unique_together = ('project', 'user')
    
    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"
