import unittest

from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_lista_pequena(self):
        lista = [5, 2, 4, 1, 3]

        resultado = bubble_sort(lista)

        self.assertEqual(resultado, [1, 2, 3, 4, 5])

    def test_lista_grande(self):
        lista = list(range(150, 0, -1))

        resultado = bubble_sort(lista)

        self.assertEqual(resultado, list(range(1, 151)))

    def test_lista_vacia(self):
        lista = []

        resultado = bubble_sort(lista)

        self.assertEqual(resultado, [])

    def test_parametro_no_es_lista(self):
        with self.assertRaises(TypeError):
            bubble_sort("esto no es una lista")


if __name__ == "__main__":
    unittest.main()