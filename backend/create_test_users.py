import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from authentication.models import User
from projects.models import Project, ProjectMember
from tasks.models import Task, TaskComment
from notifications.models import Notification

# Crear usuarios
admin = User.objects.create_user(
    username='admin_test',
    email='admin@test.com',
    password='admin123',
    first_name='Admin',
    last_name='Test',
    role='admin'
)

collab1 = User.objects.create_user(
    username='maria_garcia',
    email='maria@test.com',
    password='test123',
    first_name='María',
    last_name='García',
    role='collaborator'
)

collab2 = User.objects.create_user(
    username='carlos_lopez',
    email='carlos@test.com',
    password='test123',
    first_name='Carlos',
    last_name='López',
    role='collaborator'
)

viewer1 = User.objects.create_user(
    username='ana_martinez',
    email='ana@test.com',
    password='test123',
    first_name='Ana',
    last_name='Martínez',
    role='viewer'
)

viewer2 = User.objects.create_user(
    username='luis_rodriguez',
    email='luis@test.com',
    password='test123',
    first_name='Luis',
    last_name='Rodríguez',
    role='viewer'
)

viewer3 = User.objects.create_user(
    username='elena_fernandez',
    email='elena@test.com',
    password='test123',
    first_name='Elena',
    last_name='Fernández',
    role='viewer'
)

print("✅ Usuarios creados!")
print("Admin: admin@test.com / admin123")
print("Colaboradores: maria@test.com, carlos@test.com / test123")
print("Visores: ana@test.com, luis@test.com, elena@test.com / test123")
