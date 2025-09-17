import { z } from 'zod';

export const loginSchema = z.object({
  email: z.string().email('Email inválido'),
  password: z.string().min(1, 'La contraseña es requerida'),
});

export const registerSchema = z.object({
  username: z.string().min(3, 'El nombre de usuario debe tener al menos 3 caracteres'),
  email: z.string().email('Email inválido'),
  password: z.string().min(8, 'La contraseña debe tener al menos 8 caracteres'),
  password_confirm: z.string(),
  first_name: z.string().optional(),
  last_name: z.string().optional(),
  role: z.enum(['admin', 'collaborator', 'viewer']),
}).refine((data) => data.password === data.password_confirm, {
  message: 'Las contraseñas no coinciden',
  path: ['password_confirm'],
});

export const projectSchema = z.object({
  name: z.string().min(1, 'El nombre es requerido'),
  description: z.string().min(1, 'La descripción es requerida'),
  start_date: z.string().min(1, 'La fecha de inicio es requerida'),
  end_date: z.string().min(1, 'La fecha de fin es requerida'),
  status: z.enum(['pending', 'in_progress', 'completed', 'cancelled']),
});

export const taskSchema = z.object({
  name: z.string().min(1, 'El nombre es requerido'),
  description: z.string().min(1, 'La descripción es requerida'),
  status: z.enum(['pending', 'in_progress', 'completed']),
  project: z.number(),
  assigned_to_id: z.number().optional(),
  due_date: z.string().min(1, 'La fecha de vencimiento es requerida'),
});

export const commentSchema = z.object({
  content: z.string().min(1, 'El comentario es requerido'),
});

export type LoginFormData = z.infer<typeof loginSchema>;
export type RegisterFormData = z.infer<typeof registerSchema>;
export type ProjectFormData = z.infer<typeof projectSchema>;
export type TaskFormData = z.infer<typeof taskSchema>;
export type CommentFormData = z.infer<typeof commentSchema>;
