from django.contrib import admin
from apps.ecommerce.models import Category, Photo, Product, Comment


# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Product)
admin.site.register(Comment)