from tests.test_setup_base import TestSetup
from rest_framework import status
class TaskTestcas(TestSetup):
    def test_get_all_task(self):
        response = self.client.get(self.url_task, format='json')
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_only_task(self):
        response = self.client.get(f'{self.url_task}{self.task.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_remove_task_any(self):
        """
        si el usuario que va a hacer la eliminacion no es el mismo que creo la terea no lo puede hacer
        """
        response = self.client.delete(f'{self.url_task}{self.task.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_remove_task_only_created_task(self):
        """
        si el usuario que va a hacer la eliminacion es el mismo que creo la terea SI lo puede hacer
        """
        response = self.client.delete(f'{self.url_task}{self.task_1.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_only_five_task_for_project(self):
        task = {'task_creator':self.user_2.id,
            'assigned':self.user.id,
            'project':self.project_2.id,
            'name':'testttt',
            'description':'nda po ahira',
            'date_start':'2023-06-1',
            'date_end':'2023-12-31'
        }

        response = self.client.post(f'{self.url_task}', task, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




