import api from './api';
import { NotificationResponse } from '../types/notification';

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
    return response.data.results.filter((n: any) => !n.is_read).length;
  }
};
