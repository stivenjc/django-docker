from rest_framework import routers
from django.urls import path, include
from apps.ecommerce.views import ProductViewSet, CommentViewSet

app_name = "ecommerce"

router = routers.DefaultRouter()
router.register("product", ProductViewSet, basename="product")
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]