from rest_framework.serializers import ModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from apps.biblioteca.models import Authors, Books, LendBooks
from apps.users.UserSerializers import UserSerializer


class AuthorsSerializers(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class BooksCreateSerializers(ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'name', 'authors', 'is_free', 'created', 'modified']


class BooksListSerializers(ModelSerializer):
    authors_all = AuthorsSerializers(source='authors', many=True, read_only=True)
    class Meta:
        model = Books
        fields = ['id', 'name', 'authors_all', 'is_free', 'created', 'modified']


class LendBooksCreateSerializers(ModelSerializer):
    class Meta:
        model = LendBooks
        fields = [
            'id', 'books', 'prestador', 'receptor', 'fecha_prestamo', 'fecha_devolucion', 'created',
            'modified']

    def validate_books(self, books):
        for id_book in books:
            book = get_object_or_404(Books, id=id_book.id)
            if not book.is_free:
                raise serializers.ValidationError(
                    {f"!El libro {book.name} en estos momentos no esta disponible"})
        return books


class LendBooksListSerializers(ModelSerializer):
    books_all = BooksListSerializers(source='books', many=True)
    prestador_data = UserSerializer(source='prestador')
    receptor_data = UserSerializer(source='receptor')

    class Meta:
        model = LendBooks
        fields = ['id', 'books_all', 'prestador_data', 'receptor_data', 'fecha_prestamo', 'fecha_devolucion', 'created',
                  'modified']
