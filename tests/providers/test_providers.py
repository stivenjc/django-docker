from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

class EmailProvider(BaseProvider):
    def custom_email(self, name):
        return f'{name.title()}@gmail.com'