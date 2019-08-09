import unittest


class Test_Ruleta(unittest.TestCase):
    def test_numeros(self, numero):
        self.assertTrue(numero >= 0 and numero <= 36)


if __name__ == '__main__':
    unittest.main()
