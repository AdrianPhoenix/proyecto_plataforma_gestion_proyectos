from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modelo de usuario personalizado con sistema de roles.
    Extiende AbstractUser para incluir roles específicos del sistema.
    """
    ROLE_CHOICES = [
        ('admin', 'Administrator'),        # Control total del sistema
        ('collaborator', 'Collaborator'),  # Puede crear y editar tareas
        ('viewer', 'Viewer'),             # Solo puede ver proyectos y tareas
    ]
    
    # Email único para autenticación
    email = models.EmailField(unique=True)
    # Rol que determina los permisos del usuario
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    # Timestamps automáticos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Configuración para usar email como campo de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        """Representación string del usuario."""
        return f"{self.username} ({self.email})"
