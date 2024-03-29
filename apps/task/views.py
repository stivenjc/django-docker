from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from config.utils.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
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
    queryset = Task.objects.filter(is_active=True).select_related('task_creator', 'assigned', 'project').order_by('created')

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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data['task_creator'] = request.user.id
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        solo la persoan que lo creo tien derecho a eliminarlo
        """
        instance = self.get_object()
        user = self.request.user
        if not instance.is_active:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        instance.is_active = False
        instance.save()
        if user != instance.task_creator:
            return Response({'detail': 'No tienes permiso para eliminar este proyecto.'}, status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DownloadPDFTask(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id_task, *args, **kwargs):
        task = get_object_or_404(Task, id=id_task)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="task_details.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        story = []

        styles = getSampleStyleSheet()
        title_style = styles['Title']
        content_style = ParagraphStyle(
            'Content',
            parent=styles['BodyText'],
            spaceBefore=10,
            spaceAfter=10
        )

        # Agregar campos al PDF con estilos
        story.append(Paragraph('Detalles de la tarea', title_style))
        story.append(Paragraph(f'Nombre: {task.name}', content_style))
        story.append(Paragraph(f'Descripción: {task.description}', content_style))
        story.append(Paragraph(f'Creador de la tarea: {task.task_creator.first_name}', content_style))
        story.append(Paragraph(f'Asignado a: {task.assigned.first_name}', content_style))
        story.append(Paragraph(f'Proyecto: {task.project.name}', content_style))
        story.append(Paragraph(f'Fecha de inicio: {task.date_start}', content_style))
        story.append(Paragraph(f'Fecha de fin: {task.date_end}', content_style))

        doc.build(story)
        return response




