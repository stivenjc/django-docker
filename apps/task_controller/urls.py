from rest_framework import routers
from django.urls import path, include
from apps.task_controller.views import TaskControllerViewSet

app_name = "controller"

router = routers.DefaultRouter()
router.register("", TaskControllerViewSet, basename="controller")

urlpatterns = [
    path("", include(router.urls)),
]