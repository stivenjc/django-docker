from rest_framework import routers
from django.urls import path, include
from apps.users.views import ListUserApiView

app_name = "api"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("users/", include("apps.users.urls", namespace="users")),
    path("projects/", include("apps.projects.urls", namespace="projects")),
    path("task/", include("apps.task.urls", namespace="task")),
]