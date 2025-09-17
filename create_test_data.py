#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta

# Configurar Django
sys.path.append('/home/adrian/Documentos/adrian/devProjects/proyecto_plataforma_gestion_proyectos/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
django.setup()

from authentication.models import User
from projects.models import Project, ProjectMember
from tasks.models import Task, TaskComment
from notifications.models import Notification

def create_test_data():
    print("🚀 Creando datos de prueba...")
    
    # 1. Crear usuarios
    print("👥 Creando usuarios...")
    
    # Admin
    admin = User.objects.create_user(
        username='admin_user',
        email='admin@projecthub.com',
        password='admin123',
        first_name='Admin',
        last_name='Principal',
        role='admin'
    )
    
    # Colaboradores
    collab1 = User.objects.create_user(
        username='colaborador1',
        email='collab1@projecthub.com',
        password='collab123',
        first_name='María',
        last_name='García',
        role='collaborator'
    )
    
    collab2 = User.objects.create_user(
        username='colaborador2',
        email='collab2@projecthub.com',
        password='collab123',
        first_name='Carlos',
        last_name='López',
        role='collaborator'
    )
    
    # Visores
    viewer1 = User.objects.create_user(
        username='visor1',
        email='viewer1@projecthub.com',
        password='viewer123',
        first_name='Ana',
        last_name='Martínez',
        role='viewer'
    )
    
    viewer2 = User.objects.create_user(
        username='visor2',
        email='viewer2@projecthub.com',
        password='viewer123',
        first_name='Luis',
        last_name='Rodríguez',
        role='viewer'
    )
    
    viewer3 = User.objects.create_user(
        username='visor3',
        email='viewer3@projecthub.com',
        password='viewer123',
        first_name='Elena',
        last_name='Fernández',
        role='viewer'
    )
    
    print(f"✅ Creados 6 usuarios: 1 admin, 2 colaboradores, 3 visores")
    
    # 2. Crear proyectos
    print("📋 Creando proyectos...")
    
    project1 = Project.objects.create(
        name='Sistema de Gestión Web',
        description='Desarrollo de una plataforma web completa para gestión empresarial',
        start_date='2025-01-15',
        end_date='2025-06-30',
        status='in_progress',
        created_by=admin
    )
    
    project2 = Project.objects.create(
        name='App Mobile E-commerce',
        description='Aplicación móvil para comercio electrónico con React Native',
        start_date='2025-02-01',
        end_date='2025-08-15',
        status='pending',
        created_by=admin
    )
    
    project3 = Project.objects.create(
        name='Dashboard Analytics',
        description='Panel de control con métricas y reportes en tiempo real',
        start_date='2025-01-01',
        end_date='2025-04-30',
        status='completed',
        created_by=collab1
    )
    
    print(f"✅ Creados 3 proyectos")
    
    # 3. Agregar miembros a proyectos
    print("👨‍💼 Asignando miembros a proyectos...")
    
    # Proyecto 1 - Todos los usuarios
    ProjectMember.objects.create(project=project1, user=admin, role='admin')
    ProjectMember.objects.create(project=project1, user=collab1, role='collaborator')
    ProjectMember.objects.create(project=project1, user=collab2, role='collaborator')
    ProjectMember.objects.create(project=project1, user=viewer1, role='viewer')
    ProjectMember.objects.create(project=project1, user=viewer2, role='viewer')
    
    # Proyecto 2 - Algunos usuarios
    ProjectMember.objects.create(project=project2, user=admin, role='admin')
    ProjectMember.objects.create(project=project2, user=collab1, role='collaborator')
    ProjectMember.objects.create(project=project2, user=viewer3, role='viewer')
    
    # Proyecto 3 - Colaborador como admin
    ProjectMember.objects.create(project=project3, user=collab1, role='admin')
    ProjectMember.objects.create(project=project3, user=collab2, role='collaborator')
    ProjectMember.objects.create(project=project3, user=viewer1, role='viewer')
    
    print(f"✅ Miembros asignados a proyectos")
    
    # 4. Crear tareas
    print("✅ Creando tareas...")
    
    # Tareas Proyecto 1
    task1 = Task.objects.create(
        name='Diseño de Base de Datos',
        description='Crear el esquema de base de datos y relaciones entre entidades',
        status='completed',
        project=project1,
        assigned_to=collab1,
        created_by=admin,
        due_date=datetime.now() + timedelta(days=7)
    )
    
    task2 = Task.objects.create(
        name='Desarrollo API REST',
        description='Implementar endpoints de la API con Django REST Framework',
        status='in_progress',
        project=project1,
        assigned_to=collab2,
        created_by=admin,
        due_date=datetime.now() + timedelta(days=14)
    )
    
    task3 = Task.objects.create(
        name='Frontend React',
        description='Desarrollar interfaz de usuario con React y TypeScript',
        status='pending',
        project=project1,
        assigned_to=collab1,
        created_by=admin,
        due_date=datetime.now() + timedelta(days=21)
    )
    
    # Tareas Proyecto 2
    task4 = Task.objects.create(
        name='Prototipo UI/UX',
        description='Crear wireframes y mockups de la aplicación móvil',
        status='in_progress',
        project=project2,
        assigned_to=collab1,
        created_by=admin,
        due_date=datetime.now() + timedelta(days=10)
    )
    
    task5 = Task.objects.create(
        name='Setup React Native',
        description='Configurar proyecto base con React Native y dependencias',
        status='pending',
        project=project2,
        assigned_to=None,
        created_by=admin,
        due_date=datetime.now() + timedelta(days=5)
    )
    
    # Tareas Proyecto 3
    task6 = Task.objects.create(
        name='Integración Charts',
        description='Implementar gráficos interactivos con Chart.js',
        status='completed',
        project=project3,
        assigned_to=collab2,
        created_by=collab1,
        due_date=datetime.now() - timedelta(days=5)
    )
    
    print(f"✅ Creadas 6 tareas")
    
    # 5. Crear comentarios
    print("💬 Creando comentarios...")
    
    TaskComment.objects.create(
        task=task1,
        user=collab1,
        content='He completado el diseño inicial de la base de datos. Incluye todas las tablas principales y sus relaciones.'
    )
    
    TaskComment.objects.create(
        task=task1,
        user=admin,
        content='Excelente trabajo María! El esquema se ve muy bien estructurado.'
    )
    
    TaskComment.objects.create(
        task=task2,
        user=collab2,
        content='Estoy trabajando en los endpoints de autenticación. Debería tenerlos listos para mañana.'
    )
    
    TaskComment.objects.create(
        task=task4,
        user=collab1,
        content='Los wireframes están casi listos. Necesito feedback sobre la navegación principal.'
    )
    
    TaskComment.objects.create(
        task=task6,
        user=collab2,
        content='Charts implementados correctamente. Incluye gráficos de barras, líneas y pie charts.'
    )
    
    TaskComment.objects.create(
        task=task6,
        user=collab1,
        content='Perfecto Carlos! Los gráficos se ven geniales y son muy interactivos.'
    )
    
    print(f"✅ Creados 6 comentarios")
    
    # 6. Crear notificaciones
    print("🔔 Creando notificaciones...")
    
    Notification.objects.create(
        user=collab1,
        type='task_assigned',
        title='Nueva tarea asignada',
        message='Se te ha asignado la tarea "Frontend React" en el proyecto Sistema de Gestión Web',
        task_id=task3.id,
        project_id=project1.id
    )
    
    Notification.objects.create(
        user=collab2,
        type='task_assigned',
        title='Nueva tarea asignada',
        message='Se te ha asignado la tarea "Desarrollo API REST" en el proyecto Sistema de Gestión Web',
        task_id=task2.id,
        project_id=project1.id
    )
    
    Notification.objects.create(
        user=admin,
        type='task_completed',
        title='Tarea completada',
        message='María García ha completado la tarea "Diseño de Base de Datos"',
        task_id=task1.id,
        project_id=project1.id
    )
    
    Notification.objects.create(
        user=collab1,
        type='project_assigned',
        title='Agregado a proyecto',
        message='Has sido agregado al proyecto "App Mobile E-commerce" como colaborador',
        project_id=project2.id
    )
    
    Notification.objects.create(
        user=viewer3,
        type='project_assigned',
        title='Agregado a proyecto',
        message='Has sido agregado al proyecto "App Mobile E-commerce" como visor',
        project_id=project2.id
    )
    
    Notification.objects.create(
        user=collab1,
        type='comment_added',
        title='Nuevo comentario',
        message='Admin Principal ha comentado en la tarea "Diseño de Base de Datos"',
        task_id=task1.id,
        project_id=project1.id
    )
    
    Notification.objects.create(
        user=admin,
        type='comment_added',
        title='Nuevo comentario',
        message='Carlos López ha comentado en la tarea "Desarrollo API REST"',
        task_id=task2.id,
        project_id=project1.id
    )
    
    # Algunas notificaciones no leídas
    Notification.objects.create(
        user=collab2,
        type='project_updated',
        title='Proyecto actualizado',
        message='El proyecto "Sistema de Gestión Web" ha sido actualizado',
        project_id=project1.id,
        is_read=False
    )
    
    Notification.objects.create(
        user=viewer1,
        type='task_completed',
        title='Tarea completada',
        message='Carlos López ha completado la tarea "Integración Charts"',
        task_id=task6.id,
        project_id=project3.id,
        is_read=False
    )
    
    print(f"✅ Creadas 9 notificaciones")
    
    print("\n🎉 ¡Datos de prueba creados exitosamente!")
    print("\n📊 Resumen:")
    print(f"   👥 Usuarios: {User.objects.count()}")
    print(f"   📋 Proyectos: {Project.objects.count()}")
    print(f"   👨‍💼 Miembros de proyecto: {ProjectMember.objects.count()}")
    print(f"   ✅ Tareas: {Task.objects.count()}")
    print(f"   💬 Comentarios: {TaskComment.objects.count()}")
    print(f"   🔔 Notificaciones: {Notification.objects.count()}")
    
    print("\n🔑 Credenciales de acceso:")
    print("   Admin: admin@projecthub.com / admin123")
    print("   Colaborador 1: collab1@projecthub.com / collab123")
    print("   Colaborador 2: collab2@projecthub.com / collab123")
    print("   Visor 1: viewer1@projecthub.com / viewer123")
    print("   Visor 2: viewer2@projecthub.com / viewer123")
    print("   Visor 3: viewer3@projecthub.com / viewer123")

if __name__ == '__main__':
    create_test_data()
