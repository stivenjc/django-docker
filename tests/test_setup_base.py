from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.projects.models import Project
from apps.ecommerce.models import Category, Product
from config.utils.choices import ROL
from apps.users.models import User
from apps.task.models import Task
from tests.factories import UserFactory, UseSuperFactory
from django.contrib.auth.models import Group

fake = Faker()


class TestSetup(APITestCase):

    def setUp(self):
        """
        esto es lo primero que se ejecta antes de los test, se hace lo que tengas que hacer, por ejmplo crear
        datos en la base de datos de pruebas para poder que despues en los tes tengas datos que probar
        """

        # --------------------------user----------------------------#

        intermedio = Group.objects.create(name='Intermedio')

        self.login_url = reverse('login')
        self.user = User.objects.create_superuser(
            first_name=fake.first_name(),
            email='jimenezC@gmail.com',
            last_name=fake.last_name(),
            password='adrian',
        )
        self.user_2 = User.objects.create_user(
            first_name=fake.first_name(),
            email='jimenezCardenas@gmail.com',
            last_name=fake.last_name(),
            password='adrian',
        )
        self.user.groups.add(intermedio)
        self.user_2.groups.add(intermedio)

        response = self.client.post(self.login_url,
                                    {'email': 'jimenezC@gmail.com', 'password': 'adrian'},
                                    format='json')
        # pdb.set_trace()

        self.assertTrue(User.objects.filter(email='jimenezC@gmail.com').exists())
        self.assertTrue(self.user.check_password('adrian'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data['token']

        # de esta manera todas vista tendran acceso al toque
        #self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')

        self.Token = {'Authorization': f'Token {self.token}'}

        # self.client = Client()
        self.user_common = UserFactory.create()
        self.super_user = UseSuperFactory.create()

        # ------------------------------------proejct---------------------------------------#

        # self.url_project = '/api/projects/'
        self.url_project = reverse('api:projects:project-list')

        self.project = Project.objects.create(
            name=fake.catch_phrase(),
            created_user=self.user,
            date_start='2023-06-23',
            date_end='2023-12-31',
        )

        self.project_2 = Project.objects.create(
            name=fake.catch_phrase(),
            created_user=self.user,
            date_start='2023-06-30',
            date_end='2023-12-23',
        )

        # ---------------------------------------task------------------------------------------#

        self.url_task = reverse('api:task:task-list')

        self.task_1 = Task.objects.create(
            task_creator=self.user,
            assigned=self.user_2,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        self.task = Task.objects.create(
            task_creator=self.user_2,
            assigned=self.user,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        self.task_2 = Task.objects.create(
            task_creator=self.user_2,
            assigned=self.user,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        self.task_3 = Task.objects.create(
            task_creator=self.user_2,
            assigned=self.user,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        self.task_4 = Task.objects.create(
            task_creator=self.user_2,
            assigned=self.user,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        self.task_6 = Task.objects.create(
            task_creator=self.user_2,
            assigned=self.user,
            project=self.project_2,
            name=fake.catch_phrase(),
            description=fake.text(),
            date_start='2023-06-1',
            date_end='2023-12-31'
        )

        # -------------------ecommerce-----------------------------

        self.vendedor = User.objects.create_user(
            first_name=fake.first_name(),
            email='vendedor@gmail.com',
            last_name=fake.last_name(),
            password='adrian',
            role=ROL[1][0]
        )

        self.persona_comun = User.objects.create_user(
            first_name=fake.first_name(),
            email='comun@gmail.com',
            last_name=fake.last_name(),
            password='adrian',
        )
        self.categoria = Category.objects.create(name='electrodomesticos')

        self.product = Product.objects.create(
            name='prueba',
            price= "1000",
            category=self.categoria,
            description= "no sees",
            number_of_units= 1,
            created_by= self.vendedor
        )

        respo = self.client.post(self.login_url,
                                    {'email': 'vendedor@gmail.com', 'password': 'adrian'},
                                    format='json')

        self.token_vendedor = respo.data['token']

        self.token_vendedor = {'Authorization': f'Token {self.token_vendedor}'}



        self.url_ecommerce = reverse('api:ecommerce:product-list')
        return super().setUp()
