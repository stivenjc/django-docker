from rest_framework import routers
from django.urls import path, include
from apps.users.views import ListUserApiView

app_name = "users"

router = routers.DefaultRouter()
router.register("", ListUserApiView, basename="user-list")

urlpatterns = [
    path("", include(router.urls)),
]