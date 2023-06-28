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


