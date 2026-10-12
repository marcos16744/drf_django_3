
from django.test import TestCase

from usuarios.serializer import RegistroSerializer


class RegistroSerializerTest(TestCase):

    def test_criar_usuario(self):
        dados = {
            "username": "marcos",
            "password": "12345678"
        }

        serializer = RegistroSerializer(data=dados)

        self.assertTrue(serializer.is_valid())

        usuario = serializer.save()

        self.assertEqual(usuario.username, "marcos")

        self.assertTrue(
            usuario.check_password("12345678")
        )

    # Verifica se o serializer rejeita dados sem username
    def test_usuario_sem_username(self):
        dados = {
            "password": "12345678"
        }

        serializer = RegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
