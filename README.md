# 🚀 ProjectHub - Plataforma de Gestión de Proyectos

Una aplicación web fullstack moderna para la gestión de proyectos y tareas con sistema de roles y colaboración en tiempo real.

![Django](https://img.shields.io/badge/Django-5.2.6-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-green)
![Status](https://img.shields.io/badge/Status-Production-brightgreen)

## 🌐 **URLs de Producción**

- **🌍 Frontend**: https://proyecto-plataforma-gestion-proyect.vercel.app
- **🔧 Backend**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app
- **📡 API**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app/api
- **⚙️ Admin**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app/admin

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
- **Python 3.11**

### Frontend
- **React 19** + **TypeScript**
- **Vite** + **Tailwind CSS**
- **React Router DOM**
- **React Hook Form** + **Zod**
- **Axios**

## 🚀 Despliegue

### Producción
- **Backend**: [Railway](https://railway.app) ✅ **DESPLEGADO**
- **Frontend**: [Vercel](https://vercel.com) ✅ **DESPLEGADO**
- **Base de datos**: [Supabase](https://supabase.com) ✅ **ACTIVA**

Ver [DEPLOY.md](./DEPLOY.md) para instrucciones completas.

## 🌿 **Ramas del Proyecto**

- **`main`** - 🌟 Producción (estable)
- **`development`** - 🔧 Desarrollo (nuevas features)
- **`backup`** - 💾 Respaldo (código estable)

### Flujo de Trabajo
```bash
git checkout development    # Trabajar en desarrollo
git checkout main          # Cambiar a producción
git merge development      # Mergear cuando esté listo
```

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
│   └── runtime.txt        # Python 3.11
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
- Python 3.11+
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
- **Frontend**: https://proyecto-plataforma-gestion-proyect.vercel.app
- **Backend**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app
- **Admin**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app/admin

## 🧪 Testing

El proyecto incluye un script de pruebas completas:

```bash
./test_complete_system.sh
```

## 📊 **Estado del Proyecto**

✅ **Backend**: Desplegado y funcionando  
✅ **Frontend**: Desplegado y funcionando  
✅ **Base de datos**: Conectada y operativa  
✅ **Autenticación**: JWT funcionando  
✅ **CORS**: Configurado correctamente  
✅ **API**: Todos los endpoints activos  

## 📄 Licencia

Este proyecto es parte de una prueba técnica fullstack.

## 👨‍💻 Autor

Desarrollado con ❤️ por **AdrianPhoenix** usando las mejores prácticas de desarrollo fullstack.

---

⭐ **¡Dale una estrella si te gusta el proyecto!**

**🎯 Proyecto 100% funcional en producción** - Septiembre 2025
