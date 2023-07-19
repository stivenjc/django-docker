from django.db import models
from django.db.models import CharField, ForeignKey, PROTECT, DateField, ManyToManyField, BooleanField
from apps.users.models import User
from datetime import date
from config.utils.models import BaseModel


class Authors(BaseModel):
    name = CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if hoy.month < self.fecha_nacimiento.month or (hoy.month == self.fecha_nacimiento.month and hoy.day < self.fecha_nacimiento.day):
            edad -= 1
        return edad

    class Meta:
        db_table = 'Authors'

    def __str__(self):
        return self.name

class Books(BaseModel):
    name = CharField(max_length=50, unique=True)
    authors = ManyToManyField(Authors)
    is_free = BooleanField(default=True)


    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name

class LendBooks(BaseModel):
    books = ManyToManyField(Books)
    prestador = ForeignKey(User, on_delete=PROTECT, related_name='prestamos_realizados')
    receptor = ForeignKey(User, on_delete=PROTECT, related_name='prestamos_recibidos')
    fecha_prestamo = DateField()
    fecha_devolucion = DateField()

    class Meta:
        db_table = 'Pestamos_libros'

    def __str__(self):
        return f'Prestador: {self.prestador.email} -- Receptor: {self.receptor.email}'


