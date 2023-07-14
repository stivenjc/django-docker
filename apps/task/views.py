from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from config.utils.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Project
from apps.task.models import Task
from apps.task.serializers import TaskSerializers, TaskCreateSerializers
from apps.users.models import User


class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    def get_serializer_class(self):
        if self.action in "create":
            return TaskCreateSerializers
        elif self.action in ("update", "partial_update"):
            return TaskCreateSerializers
        elif self.action in ("list", "retrieve"):
            return TaskSerializers

    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = Task.objects.select_related('task_creator', 'assigned', 'project')

    def create(self, request, *args, **kwargs):
        # data = request.data
        # assigned = get_object_or_404(User, id=data.get('assigned'))
        # proejct = get_object_or_404(Project, id=data.get('project'))
        # data = {
        #     'task_creator': request.user.id, 'assigned': assigned.id, 'project': proejct.id, 'name': data.get('name'), 'description': data.get('description'),
        #     'date_start': data.get('date_start'), 'date_end': data.get('date_end')
        # }
        # serializer = self.get_serializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # print(serializer.data)
        # return Response(serializer.data)

        request.data['task_creator'] = request.user.id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = True if request.method == 'PATCH' else False
        instance = self.get_object()
        request.data['task_creator'] = request.user.id
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        """
        solo la persoan que lo creo tien derecho a eliminarlo
        """
        instance = self.get_object()
        user = self.request.user
        if user != instance.task_creator:
            return Response({'detail': 'No tienes permiso para eliminar este proyecto.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
