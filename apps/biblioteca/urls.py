from rest_framework import routers
from django.urls import path, include
from apps.biblioteca.views import LendBooksViewSet, BookViewSet, AuthorsViewSet

app_name = "library"

router = routers.DefaultRouter()
router.register("prestamos", LendBooksViewSet, basename="library")
router.register("books", BookViewSet, basename="books")
router.register("authors", AuthorsViewSet, basename="authors")

urlpatterns = [
    path("", include(router.urls)),
]