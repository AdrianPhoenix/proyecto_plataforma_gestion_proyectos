from .models import Notification

class NotificationService:
    @staticmethod
    def create_notification(user, notification_type, title, message, task_id=None, project_id=None):
        """Crear una nueva notificación"""
        return Notification.objects.create(
            user=user,
            type=notification_type,
            title=title,
            message=message,
            task_id=task_id,
            project_id=project_id
        )
    
    @staticmethod
    def notify_task_assigned(task):
        """Notificar cuando se asigna una tarea"""
        if task.assigned_to:
            NotificationService.create_notification(
                user=task.assigned_to,
                notification_type='task_assigned',
                title='Nueva tarea asignada',
                message=f'Se te ha asignado la tarea "{task.name}" en el proyecto "{task.project.name}"',
                task_id=task.id,
                project_id=task.project.id
            )
    
    @staticmethod
    def notify_task_completed(task):
        """Notificar cuando se completa una tarea"""
        # Notificar al creador del proyecto
        NotificationService.create_notification(
            user=task.project.created_by,
            notification_type='task_completed',
            title='Tarea completada',
            message=f'La tarea "{task.name}" ha sido completada por {task.assigned_to.username if task.assigned_to else "alguien"}',
            task_id=task.id,
            project_id=task.project.id
        )
    
    @staticmethod
    def notify_project_assigned(project_member):
        """Notificar cuando se asigna a un proyecto"""
        NotificationService.create_notification(
            user=project_member.user,
            notification_type='project_assigned',
            title='Asignado a nuevo proyecto',
            message=f'Has sido asignado al proyecto "{project_member.project.name}" como {project_member.role}',
            project_id=project_member.project.id
        )
    
    @staticmethod
    def notify_comment_added(comment):
        """Notificar cuando se agrega un comentario"""
        # Notificar al asignado de la tarea (si no es quien comentó)
        if comment.task.assigned_to and comment.task.assigned_to != comment.user:
            NotificationService.create_notification(
                user=comment.task.assigned_to,
                notification_type='comment_added',
                title='Nuevo comentario en tu tarea',
                message=f'{comment.user.username} comentó en la tarea "{comment.task.name}"',
                task_id=comment.task.id,
                project_id=comment.task.project.id
            )
