from django.contrib import admin
from django.urls import path, include
from apps.users.views import LoginView
from knox.views import LogoutView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Desplige API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Jimenezcardenasad@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('docss', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("api/", include("config.api_router", namespace='api')),
    path("login", LoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(), name='logout'),
]
