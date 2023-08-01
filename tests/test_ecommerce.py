from tests.test_setup_base import TestSetup
from rest_framework import status
class EcommerceTestcas(TestSetup):

    def test_create_product_not_any(self):
        """
        personas con un rol distinto de vendedor no pueden crear product
        """
        product = {
            "name":"prueba",
            "price":"100000",
            "category":self.categoria.id,
            "created_by":self.persona_comun.id,
            "description":"nanan",
            "number_of_units":"11",
        }
        response = self.client.post(f'{self.url_ecommerce}', product, format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_only_created_and_product(self):
        """
        la persona que esta logeada tien que ser la misma que que va la misma que creola tarea para poder que
        editar el producto
        """
        data={
            'created_by': self.user_common.id
        }
        response = self.client.patch(f'{self.url_ecommerce}{self.product.id}/', data, format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_only_creator_of_product(self):
        """
        solo se puede eliminar el producto si el usuario que lo creo lo intenta eliminar
        """
        response = self.client.delete(f'{self.url_ecommerce}{self.product.id}/', format='json', headers=self.token_vendedor)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_catno_only_of_product(self):
        """
        silo intetna eliminar cualquier pesona no padra hcerlo
        """
        response = self.client.delete(f'{self.url_ecommerce}{self.product.id}/', format='json', headers=self.Token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
