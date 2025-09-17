# 🚀 ProjectHub - Plataforma de Gestión de Proyectos

Una aplicación web fullstack moderna para la gestión de proyectos y tareas con sistema de roles y colaboración en tiempo real.

![Django](https://img.shields.io/badge/Django-5.2.6-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-green)

## ✨ Características

- 🔐 **Autenticación completa** con JWT
- 👥 **Sistema de roles** (Admin, Colaborador, Visor)
- 📋 **Gestión de proyectos** con miembros
- ✅ **Gestión de tareas** con asignaciones
- 💬 **Sistema de comentarios**
- 📱 **Interfaz responsiva** y moderna
- 🔒 **Seguridad** con permisos granulares

## 🛠️ Tecnologías

### Backend
- **Django 5.2.6** + **Django REST Framework**
- **PostgreSQL** (Supabase)
- **JWT Authentication**
- **Python 3.13**

### Frontend
- **React 19** + **TypeScript**
- **Vite** + **Tailwind CSS**
- **React Router DOM**
- **React Hook Form** + **Zod**
- **Axios**

## 🚀 Despliegue

### Producción
- **Backend**: [Railway](https://railway.app) (500h gratis/mes)
- **Frontend**: [Vercel](https://vercel.com) (gratis)
- **Base de datos**: [Supabase](https://supabase.com) (gratis)

Ver [DEPLOY.md](./DEPLOY.md) para instrucciones completas.

## 🏗️ Estructura del Proyecto

```
proyecto_plataforma_gestion_proyectos/
├── backend/                 # Django API
│   ├── project_management/  # Configuración principal
│   ├── authentication/      # App de autenticación
│   ├── projects/           # App de proyectos
│   ├── tasks/              # App de tareas
│   ├── requirements.txt    # Dependencias Python
│   ├── Procfile           # Configuración Railway
│   └── railway.json       # Configuración Railway
├── frontend/               # React App
│   ├── src/
│   │   ├── components/    # Componentes reutilizables
│   │   ├── pages/        # Páginas de la aplicación
│   │   ├── context/      # Context API
│   │   ├── services/     # Servicios de API
│   │   ├── types/        # Tipos TypeScript
│   │   └── utils/        # Utilidades
│   ├── vercel.json       # Configuración Vercel
│   └── package.json      # Dependencias Node.js
├── DEPLOY.md             # Guía de despliegue
└── README.md            # Este archivo
```

## 🚀 Instalación Local

### Prerrequisitos
- Python 3.13+
- Node.js 18+
- pnpm
- Cuenta en Supabase

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Configurar .env con credenciales de Supabase
cp .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend

```bash
cd frontend
pnpm install
pnpm run dev
```

## 📚 API Endpoints

### Autenticación
- `POST /api/auth/register/` - Registro
- `POST /api/auth/login/` - Login
- `GET /api/auth/profile/` - Perfil del usuario
- `GET /api/auth/users/` - Lista de usuarios

### Proyectos
- `GET /api/projects/` - Lista de proyectos
- `POST /api/projects/` - Crear proyecto
- `GET /api/projects/{id}/` - Detalle de proyecto
- `POST /api/projects/{id}/members/` - Agregar miembro
- `DELETE /api/projects/{id}/members/{member_id}/` - Remover miembro

### Tareas
- `GET /api/tasks/` - Lista de tareas
- `POST /api/tasks/` - Crear tarea
- `GET /api/tasks/my-tasks/` - Mis tareas
- `POST /api/tasks/{id}/comments/` - Agregar comentario
- `GET /api/tasks/{id}/comments/` - Lista de comentarios

## 🔐 Roles de Usuario

- **👑 Administrador**: Control total sobre proyectos y tareas
- **👨‍💻 Colaborador**: Puede crear y editar tareas, agregar comentarios
- **👁️ Visor**: Solo puede ver proyectos y tareas

## 🌐 URLs de Acceso

### Desarrollo
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api
- **Admin Django**: http://localhost:8000/admin

### Producción
- **Frontend**: https://tu-app.vercel.app
- **Backend**: https://tu-app.railway.app
- **Admin**: https://tu-app.railway.app/admin

## 🧪 Testing

El proyecto incluye un script de pruebas completas:

```bash
./test_complete_system.sh
```

## 📄 Licencia

Este proyecto es parte de una prueba técnica fullstack.

## 👨‍💻 Autor

Desarrollado con ❤️ usando las mejores prácticas de desarrollo fullstack.

---

⭐ **¡Dale una estrella si te gusta el proyecto!**
