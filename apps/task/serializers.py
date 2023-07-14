from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.task.models import Task
from apps.users.UserSerializers import UserSerializer


class TaskSerializers(ModelSerializer):
    data_task_creator = UserSerializer(source='task_creator', read_only=True)
    data_assigned = UserSerializer(source='assigned', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'task_creator', 'data_task_creator', 'assigned', 'data_assigned', 'project','name','description','date_start','date_end','created', 'modified']


class TaskCreateSerializers(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_creator', 'project','name','description','date_start','date_end',]

    def validate_project(self, proyecto):
        if proyecto:
            num_tareas = Task.objects.filter(project=proyecto).count()

            if num_tareas >= 5:
                raise serializers.ValidationError("El proyecto ya tiene el máximo de tareas permitidas.")

        return  attrs