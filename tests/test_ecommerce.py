from tests.test_setup_base import TestSetup
from rest_framework import status
class EcommerceTestcas(TestSetup):

    def test_create_only_seller(self):
        print(self.persona_comun.role)
        product = {
            "name":"prueba",
            "price":"100000",
            "category":self.categoria.id,
            "created_by":self.persona_comun.id,
            "description":"nanan",
            "number_of_units":"11",
        }
        response = self.client.post(f'{self.url_ecommerce}', product, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
