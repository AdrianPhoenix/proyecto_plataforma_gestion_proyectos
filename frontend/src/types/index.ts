export interface User {
  id: number;
  username: string;
  email: string;
  role: 'admin' | 'collaborator' | 'viewer';
  first_name: string;
  last_name: string;
  created_at: string;
}

export interface Project {
  id: number;
  name: string;
  description: string;
  start_date: string;
  end_date: string;
  status: 'pending' | 'in_progress' | 'completed' | 'cancelled';
  created_by: User;
  members: ProjectMember[];
  tasks_count: number;
  created_at: string;
  updated_at: string;
}

export interface ProjectMember {
  id: number;
  user: User;
  role: 'admin' | 'collaborator' | 'viewer';
  joined_at: string;
}

export interface Task {
  id: number;
  name: string;
  description: string;
  status: 'pending' | 'in_progress' | 'completed';
  project: number;
  project_name: string;
  assigned_to: User | null;
  created_by: User;
  due_date: string;
  comments: TaskComment[];
  comments_count: number;
  created_at: string;
  updated_at: string;
}

export interface TaskComment {
  id: number;
  user: User;
  content: string;
  created_at: string;
  updated_at: string;
}

export interface AuthResponse {
  user: User;
  access: string;
  refresh: string;
}
