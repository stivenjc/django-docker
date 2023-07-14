from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


class CustomPagination(PageNumberPagination):
    page_size = 10  # Número de objetos por página
    page_size_query_param = 'page_size'  # Parámetro para cambiar el tamaño de la página
    max_page_size = 100  # Tamaño máximo de la página