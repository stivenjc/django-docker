import pdb
import pytest
from django.contrib.auth.hashers import make_password
# este tescade no permite usar la base de datos se utiliza cuando no es necesario acceder a la base de datos
# from unittest import TestCase
# este tescade da permiso para acceder a la base de datos
from django.test import TestCase, Client
from faker import Faker
from rest_framework import status
from tests.test_setup_base import TestSetup

from apps.users.models import User
from tests.conftest import user_creation
from tests.factories import UserFactory, UseSuperFactory

fake = Faker()


class UserTestcas(TestSetup):

    def test_creation_user(self):
        """
        simpre debe empezar el nombre del función con "test_" por combencion
        """
        self.user_common.is_staff = False
        assert self.user_common.is_staff == False
        assert self.user_common.is_active == True
        assert self.user_common.is_superuser == False


    def test_superuser(self):
        self.assertEqual(self.super_user.is_superuser, True)

    def test_get_user(self):
        response = self.client.get('/api/users/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)





# @pytest.mark.django_db
# # este decorador es para que pueda interactuar con la base de datos
# def test_creation_user(user_creation):
#     """
#     simpre debe empezar el nombre del función con "test_" por combencion
#
#     """
#     user_creation.is_staff = False
#     assert user_creation.is_staff == False
#
#
# @pytest.mark.django_db
# def test_create_super_user(user_creation):
#     user_creation.is_superuser = True
#     assert user_creation.is_superuser
#
#
# @pytest.mark.django_db
# def test_user_creation_fail():
#     with pytest.raises(Exception):
#         User.objects.create_create(
#             last_name='test_last_name',
#             password='testpassword',
#         )
