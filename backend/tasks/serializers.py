from rest_framework import serializers
from .models import Task, TaskComment
from authentication.serializers import UserSerializer
from projects.models import Project

class TaskCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskComment
        fields = ('id', 'user', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['task'] = self.context['task']
        return super().create(validated_data)

class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    project_name = serializers.CharField(source='project.name', read_only=True)
    comments = TaskCommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'project', 'project_name',
                 'assigned_to', 'assigned_to_id', 'created_by', 'due_date', 
                 'comments', 'comments_count', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def get_comments_count(self, obj):
        return obj.comments.count()

class TaskCreateSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'project', 'assigned_to_id', 'due_date')

    def create(self, validated_data):
        assigned_to_id = validated_data.pop('assigned_to_id', None)
        validated_data['created_by'] = self.context['request'].user
        
        if assigned_to_id:
            from authentication.models import User
            validated_data['assigned_to'] = User.objects.get(id=assigned_to_id)
        
        return super().create(validated_data)
