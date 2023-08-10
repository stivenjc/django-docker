from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.task_controller.models import TaskController
from config.utils.choices import STATE_TASK


class TaskControllerCreateSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['name', 'description', 'date_and_time']

    def validate_date_and_time(self, fecha_data):
        if TaskController.objects.filter(
                date_and_time__date=fecha_data.date(), state_task=STATE_TASK[0][0],
                is_active=True
        ).count() >= 5:
            raise serializers.ValidationError(
                f'Lo siento no puedes crear mas de 5 tareas para el mismo dia'
            )
        return fecha_data

    def create(self, validate_data):
        count_task = TaskController.objects.filter(
                is_active=True, state_task=STATE_TASK[0][0]
        ).count()
        if count_task >= 20:
            raise serializers.ValidationError(
                f'Lo siento no puedes tener mas 20 tareas sin terminar,'
                f' no podras crear hasta que completes o elimines algunas'
            )
        return super().create(validate_data)



class TaskControllerUpdateSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['name', 'description', 'date_and_time', 'state_task']

    def update(self, instance, validate_data):
        date_task = validate_data.get('date_and_time')
        all_data_task = TaskController.objects.filter(
            date_and_time__date=date_task.date(), state_task=STATE_TASK[0][0],
            is_active=True
        )
        id_all_task = [item.id for item in all_data_task]
        if not instance.id in id_all_task:
            if all_data_task.count() >= 5:
                raise serializers.ValidationError(
                    f'Lo siento este dia ya tiene 5 tareas no puede añadir mas hasta que las completes o elimines'
                )
        return super().update(instance, validate_data)


class TaskControllerListRetrieveSerializers(ModelSerializer):
    class Meta:
        model = TaskController
        fields = ['id', 'name', 'description', 'date_and_time', 'is_active', 'state_task', 'created', 'modified']
