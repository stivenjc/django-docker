from rest_framework.serializers import ModelSerializer
from apps.task.models import Task
from apps.users.UserSerializers import UserSerializer


class TaskSerializers(ModelSerializer):
    data_task_creator = UserSerializer(source='task_creator', read_only=True)
    data_assigned = UserSerializer(source='assigned', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'task_creator', 'data_task_creator', 'assigned', 'data_assigned', 'project','name','description','date_start','date_end','created', 'modified']