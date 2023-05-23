# Generated by Django 4.2.1 on 2023-05-12 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_name'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='4a897ddc-7a9c-4e4a-b9bb-d523bc3ce3b8', on_delete=django.db.models.deletion.PROTECT, related_name='project', to='projects.project'),
            preserve_default=False,
        ),
    ]
