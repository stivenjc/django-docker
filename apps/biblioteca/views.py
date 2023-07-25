from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from apps.biblioteca.serializers import LendBooksCreateSerializers, LendBooksListSerializers, BooksListSerializers, BooksCreateSerializers, AuthorsSerializers
from apps.biblioteca.models import LendBooks, Books, Authors
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework.response import Response
from datetime import date

class LendBooksViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = LendBooks.objects.all().select_related('prestador', 'receptor')
        receptor = self.request.query_params.get('receptor')
        past_delivery = self.request.query_params.get('past_delivery')
        if receptor:
            queryset = queryset.filter(receptor__first_name__icontains=receptor)
        if past_delivery:
            if past_delivery != "True":
                raise ValidationError({'detail':'El parámetro past_delivery debe ser True'})
            queryset = queryset.filter(fecha_devolucion__lt=date.today())

        return queryset

    def get_serializer_class(self):
        if self.action in "create":
            return LendBooksCreateSerializers
        elif self.action in ("update", "partial_update"):
            return LendBooksCreateSerializers
        elif self.action in ("list", "retrieve"):
            return LendBooksListSerializers

    def create(self, request, *args, **kwargs):
        request.data['fecha_prestamo'] = date.today()
        request.data['prestador'] = request.user.id

        id_books = request.data.get('books', [])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        for id_book in id_books:
            book = get_object_or_404(Books, id=id_book)
            book.is_free = False
            book.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        book = instance.books.all()

        for id_book in book:
            book = get_object_or_404(Books, id=id_book.id)
            book.is_free = True
            book.save()
        return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    serializer_class = BooksListSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in "create":
            return BooksCreateSerializers
        elif self.action in ("update", "partial_update"):
            return BooksCreateSerializers
        elif self.action in ("list", "retrieve"):
            return BooksListSerializers


    def get_queryset(self):
        queryset = Books.objects.all()
        is_free = self.request.query_params.get("is_free")
        if is_free:
            if is_free != "True" and is_free != "False":
                raise ValidationError({'detail':'El parámetro is_free debe ser True o False'})
            queryset = queryset.filter(is_free=is_free)

        return queryset


class AuthorsViewSet(ModelViewSet):
    serializer_class = AuthorsSerializers
    queryset = Authors.objects.all()
    permission_classes = [IsAuthenticated]