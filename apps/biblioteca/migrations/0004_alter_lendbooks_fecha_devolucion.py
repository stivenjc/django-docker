# Generated by Django 4.2.1 on 2023-07-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_remove_lendbooks_is_free_books_is_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendbooks',
            name='fecha_devolucion',
            field=models.DateField(default='2023-07-18'),
            preserve_default=False,
        ),
    ]
