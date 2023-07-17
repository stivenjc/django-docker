from rest_framework import routers
from django.urls import path, include
from apps.task.views import TaskModelViewSet, DownloadPDFTask

app_name = "task"

router = routers.DefaultRouter()
router.register("", TaskModelViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
    path("pdf-task/<uuid:id_task>/pdf", DownloadPDFTask.as_view(), name='task-pdf'),
]