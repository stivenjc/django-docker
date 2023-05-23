from rest_framework.serializers import ModelSerializer
from apps.projects.models import Project
from apps.task.serializers import TaskSerializers
from apps.users.UserSerializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    task = TaskSerializers(many=True, read_only=True)
    data_created_user = UserSerializer(source='created_user', read_only=True)
    class Meta:
        model = Project
        fields = ['id','created_user', 'data_created_user', 'name','date_start','date_end','created','modified','task']
