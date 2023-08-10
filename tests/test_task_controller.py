from tests.test_setup_base import TestSetup
from rest_framework import status
from config.utils.choices import STATE_TASK
from apps.task_controller.models import TaskController

class TaskControllerTestcas(TestSetup):
    def test_only_create_five_taks_for_one_day(self):
        data={
            'name':'preuba6',
            'description':'nosse',
            'date_and_time':'2023-07-14T09:55:00-05:00',
        }
        response = self.client.post(f'{self.url_task_controller}', data, format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_only_update_five_taks_for_one_day(self):
        """
        verficar que al actualizar que tampoco pueda cambiar la fecha a un dia que ya tiene 5 tareas
        """
        data={
            'date_and_time':'2023-07-14T09:55:00-05:00',
        }
        response = self.client.patch(f'{self.url_task_controller}{self.task_c_6.id}/', data, format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_only_create_20_taks(self):
        data={
            'name':'preuba6',
            'description':'nosse',
            'date_and_time':'2023-09-14T09:55:00-05:00',
        }
        response = self.client.post(f'{self.url_task_controller}', data, format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertGreaterEqual(TaskController.objects.filter(is_active=True, state_task=STATE_TASK[0][0]).count(), 20)