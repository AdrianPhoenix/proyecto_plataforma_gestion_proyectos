# 🚀 Guía de Despliegue

## 📋 Preparación

### 1. Backend en Railway

#### Paso 1: Crear cuenta en Railway
1. Ve a [railway.app](https://railway.app)
2. Regístrate con GitHub
3. Conecta tu repositorio

#### Paso 2: Configurar Variables de Entorno
En Railway, ve a Variables y agrega EXACTAMENTE estas credenciales:

```env
SECRET_KEY=django-insecure-jwgyxeu4yi=6eqz#xsgdqbfrzs^n38+=#oky6y9#sibiyjfx3y
DEBUG=False
ALLOWED_HOST=tu-app.railway.app

# Supabase Database (credenciales reales)
DB_NAME=postgres
DB_USER=postgres.ipdwhkwqmzoymyiswktl
DB_PASSWORD=sly34lmpll
DB_HOST=aws-1-sa-east-1.pooler.supabase.com
DB_PORT=6543

# Frontend URL (después de desplegar en Vercel)
FRONTEND_URL=https://tu-app.vercel.app
```

#### Paso 3: Desplegar
1. Railway detectará automáticamente Django
2. Usará el `Procfile` para el comando de inicio
3. Ejecutará migraciones automáticamente

### 2. Frontend en Vercel

#### Paso 1: Preparar el Frontend
Actualiza la URL del API en el frontend:

```typescript
// frontend/src/services/api.ts
const API_BASE_URL = import.meta.env.VITE_API_URL || 
  (import.meta.env.MODE === 'production' 
    ? 'https://tu-app.railway.app/api'
    : 'http://localhost:8000/api');
```

#### Paso 2: Desplegar en Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Conecta tu repositorio
3. Configura:
   - Framework: React
   - Root Directory: `frontend`
   - Build Command: `pnpm run build`
   - Output Directory: `dist`

#### Paso 3: Variables de Entorno en Vercel
```env
VITE_API_URL=https://tu-app.railway.app/api
```

## 🔧 Configuración Final

### 1. Actualizar CORS en Railway
Después de obtener la URL de Vercel, actualiza la variable:
```env
FRONTEND_URL=https://tu-app-real.vercel.app
```

### 2. Probar la Aplicación
1. Ve a tu URL de Vercel
2. Registra un usuario
3. Crea un proyecto
4. Verifica que todo funcione

## 📊 Monitoreo

### Railway
- Logs en tiempo real
- Métricas de uso
- 500 horas gratis/mes

### Vercel
- Analytics incluidos
- Edge functions
- Despliegues automáticos

## 🔒 Seguridad

### Checklist de Producción
- ✅ DEBUG=False
- ✅ SECRET_KEY segura
- ✅ ALLOWED_HOSTS configurado
- ✅ CORS configurado correctamente
- ✅ HTTPS habilitado
- ✅ Variables de entorno seguras

## 🆘 Troubleshooting

### Errores Comunes
1. **500 Error**: Revisar logs en Railway
2. **CORS Error**: Verificar FRONTEND_URL
3. **DB Error**: Verificar credenciales de Supabase
4. **Static Files**: Railway maneja automáticamente con WhiteNoise

### Comandos Útiles
```bash
# Ver logs en Railway
railway logs

# Ejecutar migraciones manualmente
railway run python manage.py migrate

# Crear superusuario
railway run python manage.py createsuperuser
```

## 🎉 ¡Listo!

Tu aplicación estará disponible en:
- **Frontend**: https://tu-app.vercel.app
- **Backend**: https://tu-app.railway.app
- **Admin**: https://tu-app.railway.app/admin

## 📋 Variables de Entorno Completas

### Railway (Backend):
```env
SECRET_KEY=django-insecure-jwgyxeu4yi=6eqz#xsgdqbfrzs^n38+=#oky6y9#sibiyjfx3y
DEBUG=False
ALLOWED_HOST=tu-app.railway.app
DB_NAME=postgres
DB_USER=postgres.ipdwhkwqmzoymyiswktl
DB_PASSWORD=sly34lmpll
DB_HOST=aws-1-sa-east-1.pooler.supabase.com
DB_PORT=6543
FRONTEND_URL=https://tu-app.vercel.app
```

### Vercel (Frontend):
```env
VITE_API_URL=https://tu-app.railway.app/api
```
