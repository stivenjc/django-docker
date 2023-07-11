from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.task.serializers import TaskSerializers
from apps.task.models import Task
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache

class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.select_related('task_creator','assigned','project')


    def destroy(self, request, *args, **kwargs):
        """
        solo la persoan que lo creo tien derecho a eliminarlo
        """
        instance = self.get_object()
        user = self.request.user
        if user != instance.task_creator:
            return Response({'detail': 'No tienes permiso para eliminar este proyecto.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
