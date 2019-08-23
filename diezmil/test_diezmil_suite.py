import unittest
from .test_diez_mil import TestDiezMil
from .test_integration import IntegrationTest


def suite():
    test_suite = unittest.TestSuite()
    # 10K
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    test_suite.addTest(unittest.makeSuite(IntegrationTest))

    return test_suite
