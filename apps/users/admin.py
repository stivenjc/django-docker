from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.models import Permission

admin.site.register(User)
admin.site.register(Permission)