from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.task.serializers import TaskSerializers
from apps.task.models import Task
from rest_framework.response import Response
from django.core.cache import cache

class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('task_creator','assigned','project')
