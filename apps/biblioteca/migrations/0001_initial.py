# Generated by Django 4.2.1 on 2023-07-18 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'db_table': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('authors', models.ManyToManyField(to='biblioteca.authors')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='LendBooks',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('books', models.ManyToManyField(to='biblioteca.books')),
                ('prestador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prestamos_realizados', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prestamos_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Pestamos_libros',
            },
        ),
    ]
