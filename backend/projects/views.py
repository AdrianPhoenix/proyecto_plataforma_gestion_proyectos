from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project, ProjectMember
from .serializers import ProjectSerializer, ProjectCreateSerializer, ProjectMemberSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Filtrar proyectos donde el usuario es miembro
        return Project.objects.filter(projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        # Crear el proyecto
        project = serializer.save()
        # Agregar automáticamente al creador como admin del proyecto
        ProjectMember.objects.create(
            project=project,
            user=self.request.user,
            role='admin'
        )

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Project.objects.filter(projectmember__user=self.request.user).distinct()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProjectCreateSerializer
        return ProjectSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_project_member(request, project_id):
    try:
        project = Project.objects.get(id=project_id, projectmember__user=request.user)
        
        # Solo admin del proyecto puede agregar miembros
        member_role = ProjectMember.objects.get(project=project, user=request.user).role
        if member_role != 'admin':
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProjectMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_project_member(request, project_id, member_id):
    try:
        project = Project.objects.get(id=project_id, projectmember__user=request.user)
        member_role = ProjectMember.objects.get(project=project, user=request.user).role
        
        if member_role != 'admin':
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        project_member = ProjectMember.objects.get(id=member_id, project=project)
        project_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except (Project.DoesNotExist, ProjectMember.DoesNotExist):
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
