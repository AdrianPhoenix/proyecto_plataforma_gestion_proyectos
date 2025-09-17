# 🚀 Guía de Despliegue - ProjectHub

Esta guía detalla el proceso completo de despliegue de la aplicación fullstack en producción.

## 🌐 **URLs de Producción Actuales**

- **Frontend**: https://proyecto-plataforma-gestion-proyect.vercel.app
- **Backend**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app
- **API**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app/api
- **Admin**: https://proyectoplataformagestionproyectos-production-a320.up.railway.app/admin

## 📋 **Stack de Producción**

- **Backend**: Railway (Django + PostgreSQL)
- **Frontend**: Vercel (React + TypeScript)
- **Base de datos**: Supabase (PostgreSQL)
- **Autenticación**: JWT
- **CORS**: Configurado para comunicación entre servicios

## 🔧 **Configuración de Railway (Backend)**

### Variables de Entorno Requeridas:
```env
SECRET_KEY=django-insecure-jwgyxeu4yi=6eqz#xsgdqbfrzs^n38+=#oky6y9#sibiyjfx3y
DEBUG=False
ALLOWED_HOST=proyectoplataformagestionproyectos-production-a320.up.railway.app
PORT=8000

# Base de datos Supabase
DB_NAME=postgres
DB_USER=postgres.ipdwhkwqmzoymyiswktl
DB_PASSWORD=sly34lmpll
DB_HOST=aws-1-sa-east-1.pooler.supabase.com
DB_PORT=6543

# Frontend URL para CORS
FRONTEND_URL=https://proyecto-plataforma-gestion-proyect.vercel.app
```

### Configuración del Proyecto:
- **Root Directory**: `backend`
- **Build Command**: Automático (Railpack)
- **Start Command**: Definido en `Procfile`
- **Python Version**: `3.11.10` (definido en `runtime.txt`)

### Archivos de Configuración:
- `Procfile`: Comando de inicio para Railway
- `runtime.txt`: Versión de Python
- `requirements.txt`: Dependencias Python

## ▲ **Configuración de Vercel (Frontend)**

### Variables de Entorno:
```env
VITE_API_URL=https://proyectoplataformagestionproyectos-production-a320.up.railway.app/api
```

### Configuración del Proyecto:
- **Framework**: Vite
- **Root Directory**: `frontend`
- **Build Command**: `pnpm run build`
- **Output Directory**: `dist`
- **Install Command**: `pnpm install`

### Archivos de Configuración:
- `vercel.json`: Configuración de rutas SPA
- `package.json`: Dependencias y scripts

## 🐘 **Configuración de Supabase (Base de Datos)**

### Credenciales de Conexión:
- **Host**: `aws-1-sa-east-1.pooler.supabase.com`
- **Puerto**: `6543`
- **Base de datos**: `postgres`
- **Usuario**: `postgres.ipdwhkwqmzoymyiswktl`
- **Contraseña**: `sly34lmpll`

### Configuración:
- **Región**: AWS South America (São Paulo)
- **Pooler**: Habilitado para conexiones concurrentes
- **SSL**: Requerido

## 🔄 **Proceso de Despliegue**

### 1. Preparación del Código
```bash
# Asegurar que estás en la rama main
git checkout main
git pull origin main

# Verificar que todos los cambios estén committeados
git status
```

### 2. Despliegue Backend (Railway)
- Los cambios en `main` se despliegan automáticamente
- Railway detecta cambios y ejecuta build automático
- Tiempo estimado: 2-5 minutos

### 3. Despliegue Frontend (Vercel)
- Los cambios en `main` se despliegan automáticamente
- Vercel ejecuta build y deploy automático
- Tiempo estimado: 1-3 minutos

### 4. Verificación Post-Despliegue
```bash
# Probar API
curl https://proyectoplataformagestionproyectos-production-a320.up.railway.app/api/auth/users/

# Probar Frontend
curl https://proyecto-plataforma-gestion-proyect.vercel.app/
```

## 🌿 **Gestión de Ramas**

### Estructura de Ramas:
- **`main`**: Producción (auto-deploy habilitado)
- **`development`**: Desarrollo y testing
- **`backup`**: Respaldo del código estable

### Flujo de Trabajo:
```bash
# Desarrollo
git checkout development
git pull origin development
# ... hacer cambios ...
git add .
git commit -m "feat: nueva funcionalidad"
git push origin development

# Deploy a producción
git checkout main
git merge development
git push origin main  # Trigger auto-deploy
```

## 🔍 **Troubleshooting**

### Errores Comunes:

#### 1. Error 502 (Bad Gateway)
- **Causa**: Aplicación no responde en el puerto correcto
- **Solución**: Verificar variable `PORT=8000` en Railway

#### 2. Error CORS
- **Causa**: Frontend no autorizado en backend
- **Solución**: Verificar `FRONTEND_URL` en variables de Railway

#### 3. Error de Base de Datos
- **Causa**: Credenciales incorrectas o conexión fallida
- **Solución**: Verificar variables `DB_*` en Railway

#### 4. Build Failure
- **Causa**: Dependencias faltantes o incompatibles
- **Solución**: Verificar `requirements.txt` y `runtime.txt`

### Logs y Monitoreo:
- **Railway**: Logs en tiempo real en el dashboard
- **Vercel**: Logs de build y runtime en el dashboard
- **Supabase**: Métricas de base de datos en el panel

## 📊 **Métricas de Rendimiento**

### Tiempos de Respuesta Objetivo:
- **API**: < 500ms
- **Frontend**: < 2s (First Contentful Paint)
- **Base de datos**: < 100ms (queries simples)

### Límites de Recursos:
- **Railway**: 500h/mes (plan gratuito)
- **Vercel**: 100GB bandwidth/mes (plan gratuito)
- **Supabase**: 500MB storage (plan gratuito)

## 🔐 **Seguridad**

### Configuraciones de Seguridad:
- **HTTPS**: Habilitado en todos los servicios
- **CORS**: Configurado específicamente para el frontend
- **JWT**: Tokens con expiración configurada
- **Variables de entorno**: Nunca expuestas en el código

### Recomendaciones:
- Rotar `SECRET_KEY` periódicamente
- Monitorear logs de acceso
- Mantener dependencias actualizadas
- Usar `DEBUG=False` en producción

## 📝 **Checklist de Despliegue**

### Pre-Despliegue:
- [ ] Código testeado localmente
- [ ] Variables de entorno configuradas
- [ ] Base de datos migrada
- [ ] CORS configurado correctamente

### Post-Despliegue:
- [ ] API responde correctamente
- [ ] Frontend carga sin errores
- [ ] Autenticación funciona
- [ ] CRUD operations funcionan
- [ ] Logs sin errores críticos

---

## 🎯 **Estado Actual: ✅ PRODUCCIÓN ESTABLE**

**Última actualización**: Septiembre 17, 2025
**Versión**: 1.0.0
**Estado**: 100% Funcional
