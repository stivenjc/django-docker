from django.db.models import Q, F
from django.shortcuts import render
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.task_controller.models import TaskController
from apps.task_controller.serializers import TaskControllerCreateSerializers, \
    TaskControllerListRetrieveSerializers, TaskControllerUpdateSerializers
from config.utils.choices import STATE_TASK
from apps.projects.Permissions import CanallTaskPermission


class TaskControllerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, CanallTaskPermission]

    def get_queryset(self):
        queryset = TaskController.objects.filter(is_active=True).order_by('-created')
        task_completed = self.request.query_params.get('task_completed')
        task_passed_time = self.request.query_params.get('task_passed_time')
        task_name = self.request.query_params.get('task_name')
        filtered_time_bout_to_end= self.request.query_params.get('filtered_time_bout_to_end')
        if task_completed:
            if task_completed != "True":
                raise ValidationError({'detail': 'El parámetro task_completed debe ser True'})
            queryset = queryset.filter(state_task=STATE_TASK[1][0])
        if task_passed_time:
            tiempo_actual = timezone.localtime()
            if task_passed_time != "True":
                raise ValidationError({'detail': 'El parámetro task_passed_time debe ser True'})
            queryset = queryset.filter(
                Q(date_and_time__lt=tiempo_actual) & Q(date_and_time__hour=F('date_and_time__hour')) &
                Q(state_task=STATE_TASK[0][0]))
        if task_name:
            queryset = queryset.filter(name__icontains=task_name)
        if filtered_time_bout_to_end:
            tiempo_actual = timezone.localtime()
            if filtered_time_bout_to_end != "True":
                raise ValidationError({'detail': 'El parámetro filtered_time_bout_to_end debe ser True'})
            queryset = queryset.filter(
                Q(date_and_time__gte=tiempo_actual) & Q(date_and_time__hour=F('date_and_time__hour')) &
                Q(state_task=STATE_TASK[0][0])
            ).order_by('date_and_time')

        return queryset

    def get_serializer_class(self):
        if self.action in "create":
            return TaskControllerCreateSerializers
        elif self.action in ("update", "partial_update"):
            return TaskControllerUpdateSerializers
        elif self.action in ("list", "retrieve"):
            return TaskControllerListRetrieveSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

