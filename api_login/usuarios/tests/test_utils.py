from django.test import TestCase

from usuarios.utils import calcular_total


class CalcularTotalTest(TestCase):

    def test_calcular_total(self):

        resultado = calcular_total(10, 3)

        self.assertEqual(resultado, 30)