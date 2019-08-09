import unittest
from uno.test_uno import TestUno


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUno))


if __name__ == '__main__':
    unittest.main()
