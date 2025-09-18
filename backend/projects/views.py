from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project, ProjectMember
from .serializers import ProjectSerializer, ProjectCreateSerializer, ProjectMemberSerializer
from notifications.services import NotificationService

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar y crear proyectos.
    GET: Retorna proyectos donde el usuario es miembro
    POST: Crea nuevo proyecto y agrega al usuario como admin
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtra proyectos donde el usuario autenticado es miembro."""
        return Project.objects.filter(projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        """Retorna serializer apropiado según el método HTTP."""
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        """Crea proyecto y agrega al usuario como administrador."""
        # Crear el proyecto
        project = serializer.save()
        # Agregar automáticamente al creador como admin del proyecto
        ProjectMember.objects.create(
            project=project,
            user=self.request.user,
            role='admin'
        )

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para operaciones CRUD en proyecto específico.
    Solo miembros del proyecto pueden acceder.
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtra proyectos donde el usuario es miembro."""
        return Project.objects.filter(projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        """Retorna serializer apropiado según el método HTTP."""
        if self.request.method in ['PUT', 'PATCH']:
            return ProjectCreateSerializer
        return ProjectSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_project_member(request, project_id):
    """
    Agrega un miembro a un proyecto.
    Solo admins del proyecto pueden agregar miembros.
    Envía notificación automática al usuario agregado.
    """
    try:
        # Verificar que el proyecto existe y el usuario es miembro
        project = Project.objects.get(id=project_id, projectmember__user=request.user)
        
        # Solo admin del proyecto puede agregar miembros
        member_role = ProjectMember.objects.get(project=project, user=request.user).role
        if member_role != 'admin':
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        # Validar y crear el nuevo miembro
        serializer = ProjectMemberSerializer(data=request.data)
        if serializer.is_valid():
            project_member = serializer.save(project=project)
            # Notificar al usuario asignado al proyecto
            NotificationService.notify_project_assigned(project_member)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_project_member(request, project_id, member_id):
    """
    Remueve un miembro de un proyecto.
    Solo admins del proyecto pueden remover miembros.
    """
    try:
        # Verificar acceso al proyecto
        project = Project.objects.get(id=project_id, projectmember__user=request.user)
        member_role = ProjectMember.objects.get(project=project, user=request.user).role
        
        # Verificar permisos de admin
        if member_role != 'admin':
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        # Remover el miembro especificado
        project_member = ProjectMember.objects.get(id=member_id, project=project)
        project_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except (Project.DoesNotExist, ProjectMember.DoesNotExist):
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
