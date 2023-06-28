#para crea los fixture para las pruebas, que se creen antes de ejecutar las pruebas

import pytest
from apps.users.models import User
from apps.projects.models import Project
from ddf import N
from faker import Faker
from tests.providers.test_providers import EmailProvider
from tests.factories import UserFactory, ProjectFactory

fake = Faker()
fake.add_provider(EmailProvider)

#hay que ponerle el decoradopr "@pytest.fixture" para que ṕueda pasarse como parametro
# @pytest.fixture
# def user_creation():
#     "crea una instacia de la tabla user pero no toca la base de datos es buena manera de hacer test unitario"
#     return N(User)


#hacer al instacia con factory_boy
@pytest.fixture
def user_creation():
    return UserFactory()


# hay que ponerle el decoradopr "@pytest.fixture" para que ṕueda pasarse como parametro
@pytest.fixture
def common_user_creation(user_creation):
    """
    creacion de datos de un usuario con datos flaso, creados por una libreria
    """
    print(user_creation.first_name)
    first_name = fake.first_name()
    return User(
        first_name=first_name,
        email=fake.custom_email(first_name),
        last_name=fake.last_name(),
        password=fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
    )

# @pytest.fixture
# @pytest.mark.django_db
# def create_project():
#     user = N(User)
#     return N(Project, created_user=user)

#hacer al instacia con factory_boy

@pytest.fixture
def create_project():
    return ProjectFactory()