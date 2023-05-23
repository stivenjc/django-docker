from rest_framework import routers
from django.urls import path, include
from apps.task.views import TaskModelViewSet

app_name = "task"

router = routers.DefaultRouter()
router.register("", TaskModelViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
]