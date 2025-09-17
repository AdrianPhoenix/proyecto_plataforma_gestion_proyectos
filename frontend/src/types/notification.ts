export interface Notification {
  id: number;
  type: 'task_assigned' | 'task_completed' | 'project_assigned' | 'comment_added' | 'project_updated';
  title: string;
  message: string;
  is_read: boolean;
  created_at: string;
  task_id?: number;
  project_id?: number;
}

export interface NotificationResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Notification[];
}
