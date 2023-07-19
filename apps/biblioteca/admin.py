from django.contrib import admin
from apps.biblioteca.models import Authors, Books, LendBooks

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(LendBooks)