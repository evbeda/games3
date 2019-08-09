import unittest
from uno.test_uno import TestUno
from craps.test_craps import TestCraps


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUno))
    test_suite.addTest(unittest.makeSuite(TestCraps))


if __name__ == '__main__':
    unittest.main()
