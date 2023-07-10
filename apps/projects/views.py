from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer
from rest_framework.response import Response


class UserModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        hacer mas eficientes las consultas cuando vas a hacer filtros con campos de leacin como en este caso.
        """
        queryset = Project.objects.select_related('created_user').prefetch_related('task')
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(created_user__email__icontains=name).select_related('created_user')

        return queryset