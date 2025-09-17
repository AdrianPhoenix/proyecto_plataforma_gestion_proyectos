from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task_list_create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:task_id>/comments/', views.add_task_comment, name='add_task_comment'),
    path('<int:task_id>/comments/list/', views.task_comments, name='task_comments'),
    path('my-tasks/', views.my_tasks, name='my_tasks'),
]
