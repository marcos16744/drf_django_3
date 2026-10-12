from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User


class RegistroEndpointTest(APITestCase):

        
    def test_registro_usuario(self):

        dados = {
            "username": "marcos",
            "password": "12345678"
        }

        response = self.client.post(
            "/registro/",
            dados,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            User.objects.filter(username="marcos").exists()
        )



    #testando sem username para ver se tem erro

    def test_registro_sem_username(self):

        dados = {
            "password": "12345678"
        }

        response = self.client.post(
            "/registro/",
            dados,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )