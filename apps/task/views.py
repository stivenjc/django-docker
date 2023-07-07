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
    queryset = Task.objects.all()


    def list(self, request, *args, **kwargs):
        cached_data = cache.get('data')
        if cached_data is not None:
            print('si esta funcionando dato guardado')
            queryset = cached_data
            cache.clear()
        else:
            print('no, todavia no esta guraddo ya se gaurdara')
            queryset = Task.objects.all()
            cache.set('data', queryset, timeout=3600)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
