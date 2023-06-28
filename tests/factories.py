import factory
from apps.users.models import User
from apps.projects.models import Project
from tests.providers.test_providers import EmailProvider
from faker import Faker


fake = Faker()
fake.add_provider(EmailProvider)



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    # email = fake.custom_email(first_name)
    email = 'jimenezcardenasad@gmail.com'
    last_name=fake.last_name()
    is_staff = True
    password='adrian'
    is_superuser = False

class UseSuperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    email = fake.custom_email(first_name)
    last_name=fake.last_name()
    password=fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    is_staff = True
    is_superuser = True


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    name = fake.catch_phrase()
    created_user = factory.SubFactory(UserFactory)
    date_start = '2023-06-23'
    date_end = '2023-12-31'