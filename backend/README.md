# Backend - Plataforma de Gestión de Proyectos

## Tecnologías
- Django 5.2.6
- Django REST Framework
- PostgreSQL (Supabase)
- JWT Authentication

## Configuración

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar variables de entorno en `.env`:
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres.your_project_ref
DB_PASSWORD=your_password
DB_HOST=aws-1-sa-east-1.pooler.supabase.com
DB_PORT=6543
```

3. Ejecutar migraciones:
```bash
python manage.py migrate
```

4. Crear superusuario:
```bash
python manage.py createsuperuser
```

5. Iniciar servidor:
```bash
python manage.py runserver
```

## API Endpoints

### Autenticación
- `POST /api/auth/register/` - Registro de usuario
- `POST /api/auth/login/` - Login
- `POST /api/auth/token/refresh/` - Refresh token
- `GET /api/auth/profile/` - Perfil del usuario
- `GET /api/auth/users/` - Lista de usuarios

### Proyectos
- `GET /api/projects/` - Lista de proyectos
- `POST /api/projects/` - Crear proyecto
- `GET /api/projects/{id}/` - Detalle de proyecto
- `PUT /api/projects/{id}/` - Actualizar proyecto
- `DELETE /api/projects/{id}/` - Eliminar proyecto
- `POST /api/projects/{id}/members/` - Agregar miembro
- `DELETE /api/projects/{id}/members/{member_id}/` - Remover miembro

### Tareas
- `GET /api/tasks/` - Lista de tareas
- `POST /api/tasks/` - Crear tarea
- `GET /api/tasks/{id}/` - Detalle de tarea
- `PUT /api/tasks/{id}/` - Actualizar tarea
- `DELETE /api/tasks/{id}/` - Eliminar tarea
- `GET /api/tasks/my-tasks/` - Mis tareas asignadas
- `POST /api/tasks/{id}/comments/` - Agregar comentario
- `GET /api/tasks/{id}/comments/list/` - Lista de comentarios

## Roles de Usuario
- **admin**: Puede crear, editar y eliminar proyectos y tareas
- **collaborator**: Puede crear y editar tareas, agregar comentarios
- **viewer**: Solo puede ver proyectos y tareas
