from django.db import models
from django.db.models import CharField, PositiveBigIntegerField, DecimalField, ForeignKey, PROTECT, DateField, \
    ManyToManyField, \
    BooleanField, TextField
from django.contrib.auth.models import AbstractUser
from apps.users.models import User
from config.utils.choices import ROL
from config.utils.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    imagen = models.ImageField(upload_to='ecommerce/fotos/')

    def __str__(self):
        return f'{self.imagen} --- {self.id}'

class Product(BaseModel):
    name = CharField(max_length=50)
    photos = ManyToManyField(Photo, blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    is_active = BooleanField(default=True)
    category = ForeignKey(Category, on_delete=PROTECT)
    created_by = ForeignKey(User, on_delete=PROTECT)
    description = TextField()
    exhausted_resource = BooleanField(default=False)
    number_of_units = PositiveBigIntegerField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.name}---${self.price}---{self.number_of_units}'


class Comment(BaseModel):
    comment = TextField()
    product = ForeignKey(Product, on_delete=PROTECT, related_name='comment')
    buyer = ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return f'{self.comment} --- {self.buyer.email}'

