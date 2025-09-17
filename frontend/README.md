# Frontend - Plataforma de Gestión de Proyectos

## Tecnologías
- Vite
- React 19
- TypeScript
- Tailwind CSS
- React Router DOM
- React Hook Form
- Zod (validaciones)
- Axios (HTTP client)

## Configuración

1. Instalar dependencias:
```bash
pnpm install
```

2. Iniciar servidor de desarrollo:
```bash
pnpm run dev
```

3. Build para producción:
```bash
pnpm run build
```

## Estructura del Proyecto

```
src/
├── components/     # Componentes reutilizables
├── pages/         # Páginas de la aplicación
├── context/       # Context API (AuthContext)
├── services/      # Servicios de API
├── types/         # Tipos TypeScript
├── utils/         # Utilidades y esquemas de validación
└── hooks/         # Custom hooks (futuro)
```

## Funcionalidades Implementadas

### Autenticación
- ✅ Login con email y contraseña
- ✅ Registro de usuarios con roles
- ✅ Context API para manejo de estado de autenticación
- ✅ Protección de rutas
- ✅ Refresh token automático

### Navegación
- ✅ Layout principal con navegación
- ✅ Rutas protegidas y públicas
- ✅ Dashboard básico
- ✅ Páginas de proyectos y tareas (estructura básica)

### Validaciones
- ✅ Esquemas Zod para formularios
- ✅ Validación en tiempo real
- ✅ Manejo de errores

## Próximos Pasos

- [ ] Implementar CRUD completo de proyectos
- [ ] Implementar CRUD completo de tareas
- [ ] Sistema de comentarios
- [ ] Gestión de miembros de proyecto
- [ ] Dashboard con estadísticas reales
- [ ] Notificaciones
- [ ] Responsive design mejorado

## Scripts Disponibles

- `pnpm run dev` - Servidor de desarrollo
- `pnpm run build` - Build para producción
- `pnpm run preview` - Preview del build
- `pnpm run lint` - Linter ESLint
