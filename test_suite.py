import unittest
from uno.test_uno import TestUno
from craps.test_craps import TestCraps
from dungeon_raiders.test_dungeon import TestDungeon
from ruleta.test_ruleta import Test_Ruleta


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUno))
    test_suite.addTest(unittest.makeSuite(TestCraps))
    test_suite.addTest(unittest.makeSuite(TestDungeon))
    test_suite.addTest(unittest.makeSuite(Test_Ruleta))


if __name__ == '__main__':
    unittest.main()
