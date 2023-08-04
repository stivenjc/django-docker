from rest_framework.serializers import ModelSerializer

from apps.task_controller.models import TaskController


class TaskControllerCreateSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['name', 'description', 'date_and_time']


class TaskControllerUpdateSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['name', 'description', 'date_and_time', 'state_task']


class TaskControllerListRetrieveSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['id', 'name', 'description', 'date_and_time', 'is_active', 'state_task', 'created', 'modified']
