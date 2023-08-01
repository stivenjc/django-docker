from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from apps.ecommerce.serializers import ProductCreateSerializer, ProductListSerializer, CommentCreateSerializer, CommentListSerializer
from apps.ecommerce.models import Product, Comment
from rest_framework.response import Response
from config.utils.choices import ROL

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in "create":
            return ProductCreateSerializer
        elif self.action in ("update", "partial_update"):
            return ProductCreateSerializer
        elif self.action in ("list", "retrieve"):
            return ProductListSerializer


    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.id
        if request.user.role != ROL[1][0]:
            return  Response({'message': 'I sorry, you cannot do this operation because you are not seller'}, status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = True if request.method == "PATCH" else False
        instance = self.get_object()
        request.data['created_by'] = request.user.id
        if instance.created_by.id != request.user.id:
            return Response({'message': 'I sorry, you cannot do actions this product'}, status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by.id != request.user.id:
            return Response({'message': 'I sorry, you cannot do actions this product'}, status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    def get_serializer_class(self):
        if self.action in "create":
            return CommentCreateSerializer
        elif self.action in ("update", "partial_update"):
            return CommentCreateSerializer
        elif self.action in ("list", "retrieve"):
            return CommentListSerializer
