import axios from 'axios';
import type { NotificationResponse, Notification } from '../types/notification';

// Crear instancia de axios para notificaciones
const API_BASE_URL = import.meta.env.VITE_API_URL || 
  (import.meta.env.MODE === 'production' 
    ? 'https://proyectoplataformagestionproyectos-production-a320.up.railway.app/api'
    : 'http://localhost:8000/api');

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const notificationService = {
  // Obtener notificaciones del usuario
  getNotifications: async (): Promise<NotificationResponse> => {
    const response = await api.get('/notifications/');
    return response.data;
  },

  // Marcar notificación como leída
  markAsRead: async (notificationId: number): Promise<void> => {
    await api.post(`/notifications/${notificationId}/read/`);
  },

  // Marcar todas como leídas
  markAllAsRead: async (): Promise<void> => {
    await api.post('/notifications/mark-all-read/');
  },

  // Obtener conteo de no leídas
  getUnreadCount: async (): Promise<number> => {
    const response = await api.get('/notifications/');
    return response.data.results.filter((n: Notification) => !n.is_read).length;
  }
};
