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
    path("library/", include("apps.biblioteca.urls", namespace="library")),
    path("ecommerce/", include("apps.ecommerce.urls", namespace="ecommerce")),
    path("task_controller/", include("apps.task_controller.urls", namespace="controller")),
]