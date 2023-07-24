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

    def create(self, validated_data):
        books = validated_data.get('books', [])
        print(books)
        for id_book in books:
            book = get_object_or_404(Books, id=id_book.id)
            if not book.is_free:
                raise serializers.ValidationError(
                    f"El libro '{book.name}' no está disponible en estos momentos.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        old_books = instance.books.all()

        old_ids = [book.id for book in old_books]

        new_books_ids = validated_data.get('books', [])

        ids_book_new = []
        for boo in new_books_ids:
            book = get_object_or_404(Books, id=boo.id)
            ids_book_new.append(book.id)

        for id_book in new_books_ids:
            book = get_object_or_404(Books, id=id_book.id)
            if not book.is_free:
                if book.id in old_ids:
                    continue
                raise serializers.ValidationError(f"El libro '{book.name}' no está disponible en estos momentos.")

        id_book_to_true = []
        for id in old_ids:
            if id not in ids_book_new:
                print('hola')
                id_book_to_true.append(id)

        self.save_false_books(id_book_to_true)

        print(id_book_to_true, ids_book_new)

        self.mark_books_as_borrowed(new_books_ids)
        instance.books.set(new_books_ids)

        return instance

    def mark_books_as_borrowed(self, books):
        for book in books:
            book.is_free = False
            book.save()

    def save_false_books(self, books):
        for id in books:
            book = get_object_or_404(Books, id=id)
            book.is_free = True
            book.save()



class LendBooksListSerializers(ModelSerializer):
    books_all = BooksListSerializers(source='books', many=True)
    prestador_data = UserSerializer(source='prestador')
    receptor_data = UserSerializer(source='receptor')

    class Meta:
        model = LendBooks
        fields = ['id', 'books_all', 'prestador_data', 'receptor_data', 'fecha_prestamo', 'fecha_devolucion', 'created',
                  'modified']
