from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListCreateView.as_view(), name='project_list_create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:project_id>/members/', views.add_project_member, name='add_project_member'),
    path('<int:project_id>/members/<int:member_id>/', views.remove_project_member, name='remove_project_member'),
]
