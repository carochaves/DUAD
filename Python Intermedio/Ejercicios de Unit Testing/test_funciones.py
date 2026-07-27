import unittest
import funciones


class TestTotalSum(unittest.TestCase):

    def test_caso_1(self):
        funciones.list_1 = [20, 30, 40, 50]
        self.assertEqual(funciones.total_sum(), 140)

    def test_caso_2(self):
        funciones.list_1 = [1, 2, 3]
        self.assertEqual(funciones.total_sum(), 6)

    def test_caso_3(self):
        funciones.list_1 = [10]
        self.assertEqual(funciones.total_sum(), 10)


class TestTurnOver(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(
            funciones.turn_over("Costa Rica"),
            "aciR atsoC"
        )

    def test_caso_2(self):
        self.assertEqual(
            funciones.turn_over("Python"),
            "nohtyP"
        )

    def test_caso_3(self):
        self.assertEqual(
            funciones.turn_over("ABC"),
            "CBA"
        )


class TestTotalUpperLower(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(
            funciones.total_upper_lower("AZUL"),
            (0, 4)
        )

    def test_caso_2(self):
        self.assertEqual(
            funciones.total_upper_lower("azul"),
            (4, 0)
        )

    def test_caso_3(self):
        self.assertEqual(
            funciones.total_upper_lower("Hola"),
            (3, 1)
        )


class TestAbcOrder(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(
            funciones.abc_order("pera-manzana-banano"),
            "banano-manzana-pera"
        )

    def test_caso_2(self):
        self.assertEqual(
            funciones.abc_order("z-y-x"),
            "x-y-z"
        )

    def test_caso_3(self):
        self.assertEqual(
            funciones.abc_order("casa-arbol-flor"),
            "arbol-casa-flor"
        )


class TestPrimeNumbers(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(
            funciones.prime_numbers([2, 3, 4, 5]),
            [2, 3, 5]
        )

    def test_caso_2(self):
        self.assertEqual(
            funciones.prime_numbers([10, 11, 12, 13]),
            [11, 13]
        )

    def test_caso_3(self):
        self.assertEqual(
            funciones.prime_numbers([17, 18, 19]),
            [17, 19]
        )


if __name__ == "__main__":
    unittest.main()