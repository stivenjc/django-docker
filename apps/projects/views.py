from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import requests
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('projects.permision_normal')

class UserModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def get_queryset(self):
        """
        hacer mas eficientes las consultas cuando vas a hacer filtros con campos de leacin como en este caso.
        """
        queryset = Project.objects.select_related('created_user').prefetch_related('task')
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(created_user__email__icontains=name)

        return queryset
    #
    # def list(self, request, *args, **kwargs):
    #     url = 'https://backend-django-docker.onrender.com/api/projects/'  # URL del endpoint que deseas consumir
    #     data = []
    #     token = '0e303e7301a25dd66f91a27126efbe33c3a307cf4e1ce648cf51ec607d2a8132'
    #     headers = {
    #         'Authorization': f'Token {token}'
    #     }
    #     try:
    #         response = requests.get(url, headers=headers)
    #         response.raise_for_status()
    #
    #         data = response.json()
    #
    #     except requests.exceptions.RequestException as e:
    #         print(f'Error al consumir el endpoint: {e}')
    #
    #     return Response(data)
