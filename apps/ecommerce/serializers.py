from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.users.UserSerializers import UserSerializer
from apps.ecommerce.models import Product, Comment, Photo
from rest_framework import serializers


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'imagen']

class CommentListSerializer(ModelSerializer):
    buyer = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment',
            'product',
            'buyer',
            'created',
            'modified'
        ]

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'comment',
            'product',
            'buyer',
            'created',
            'modified'
        ]
class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'photos',
            'price',
            'is_active',
            'category',
            'created_by',
            'description',
            'exhausted_resource',
            'number_of_units',
            'created',
            'modified'
        ]




class ProductListSerializer(ModelSerializer):
    comment = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)
    created_by=UserSerializer(read_only=True)
    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'photos',
            'comment',
            'price',
            'is_active',
            'category',
            'created_by',
            'description',
            'exhausted_resource',
            'number_of_units',
            'created',
            'modified'
        ]

    def get_comment(self, product):
        comments = Comment.objects.filter(product=product).order_by('-created')
        serializer = CommentListSerializer(comments, many=True)
        return serializer.data