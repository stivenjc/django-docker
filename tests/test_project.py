import pdb
from rest_framework import status

from apps.projects.models import Project
from tests.test_setup_base import TestSetup


class ProjectTestcas(TestSetup):

    def test_get_all_project(self):
        response = self.client.get(self.url_project, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_only_project(self):
        response = self.client.get(f'{self.url_project}{self.project.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_name_project(self):
        query_params = {'name': 'ini'}
        response = self.client.get(self.url_project, query_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        data = {
            'name': 'helllo',
            'created_user': self.user.id,
            'date_start': '2023-07-14',
            'date_end': '2023-07-14'
        }

        respo = self.client.patch(f'{self.url_project}{self.project.id}/', data, format='json')
        self.assertEqual(respo.status_code, status.HTTP_200_OK)
        self.assertNotEqual(self.project.date_start, data['date_start'])
        self.assertEqual(respo.data['name'], data['name'])
        self.assertEqual(respo.data['data_created_user']['email'], self.user.email)

        self.assertEqual(respo.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        respo = self.client.delete(f'{self.url_project}{self.project.id}/', format='json')

        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=self.project.id)

        self.assertEqual(respo.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_project(self):

        data = {
            'name': 'ProejctStivenJc',
            'created_user': self.user_2.id,
            'date_start': '2002-07-14',
            'date_end': '2023-07-14'
        }
        response = self.client.post(self.url_project, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# import pytest
# from factories import ProjectFactory
#
# def test_creation_project():
#     create_project = ProjectFactory()
#     assert create_project.created_user.is_staff == True
