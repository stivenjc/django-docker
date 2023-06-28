from rest_framework import routers
from django.urls import path, include
from apps.projects.views import UserModelViewSet

app_name = "projects"

router = routers.DefaultRouter()
router.register("", UserModelViewSet, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]