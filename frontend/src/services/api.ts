import axios from 'axios';
import type { AuthResponse, User, Project, Task, TaskComment } from '../types';
import type { LoginFormData, RegisterFormData, ProjectFormData, TaskFormData, CommentFormData } from '../utils/schemas';

// API Base URL - cambia automáticamente según el entorno
const API_BASE_URL = import.meta.env.VITE_API_URL || 
  (import.meta.env.MODE === 'production' 
    ? 'https://your-railway-app.railway.app/api'  // Cambiar por tu URL de Railway
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

// Interceptor para manejar refresh token
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        try {
          const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
            refresh: refreshToken,
          });
          localStorage.setItem('access_token', response.data.access);
          error.config.headers.Authorization = `Bearer ${response.data.access}`;
          return api.request(error.config);
        } catch {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login';
        }
      }
    }
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  login: (data: LoginFormData): Promise<AuthResponse> =>
    api.post('/auth/login/', data).then(res => res.data),
  
  register: (data: RegisterFormData): Promise<AuthResponse> =>
    api.post('/auth/register/', data).then(res => res.data),
  
  getProfile: (): Promise<User> =>
    api.get('/auth/profile/').then(res => res.data),
  
  getUsers: (): Promise<User[]> =>
    api.get('/auth/users/').then(res => res.data.results || res.data),
};

// Projects API
export const projectsAPI = {
  getProjects: (): Promise<Project[]> =>
    api.get('/projects/').then(res => res.data.results || res.data),
  
  getProject: (id: number): Promise<Project> =>
    api.get(`/projects/${id}/`).then(res => res.data),
  
  createProject: (data: ProjectFormData): Promise<Project> =>
    api.post('/projects/', data).then(res => res.data),
  
  updateProject: (id: number, data: Partial<ProjectFormData>): Promise<Project> =>
    api.put(`/projects/${id}/`, data).then(res => res.data),
  
  deleteProject: (id: number): Promise<void> =>
    api.delete(`/projects/${id}/`),
  
  addMember: (projectId: number, userId: number, role: string): Promise<any> =>
    api.post(`/projects/${projectId}/members/`, { user_id: userId, role }),
  
  removeMember: (projectId: number, memberId: number): Promise<void> =>
    api.delete(`/projects/${projectId}/members/${memberId}/`),
};

// Tasks API
export const tasksAPI = {
  getTasks: (projectId?: number): Promise<Task[]> =>
    api.get('/tasks/', { params: projectId ? { project: projectId } : {} }).then(res => res.data.results || res.data),
  
  getTask: (id: number): Promise<Task> =>
    api.get(`/tasks/${id}/`).then(res => res.data),
  
  createTask: (data: TaskFormData): Promise<Task> =>
    api.post('/tasks/', data).then(res => res.data),
  
  updateTask: (id: number, data: Partial<TaskFormData>): Promise<Task> =>
    api.put(`/tasks/${id}/`, data).then(res => res.data),
  
  deleteTask: (id: number): Promise<void> =>
    api.delete(`/tasks/${id}/`),
  
  getMyTasks: (): Promise<Task[]> =>
    api.get('/tasks/my-tasks/').then(res => Array.isArray(res.data) ? res.data : res.data.results || []),
  
  addComment: (taskId: number, data: CommentFormData): Promise<TaskComment> =>
    api.post(`/tasks/${taskId}/comments/`, data).then(res => res.data),
  
  getComments: (taskId: number): Promise<TaskComment[]> =>
    api.get(`/tasks/${taskId}/comments/list/`).then(res => res.data),
};
