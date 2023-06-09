# Generated by Django 4.2.1 on 2023-05-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_name'),
        ('task', '0002_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task', to='projects.project'),
        ),
    ]
