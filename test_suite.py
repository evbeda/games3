import unittest
from uno.test_uno import TestUno
from dungeon_raiders.test_dungeon import TestDungeon


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUno))
    test_suite.addTest(unittest.makeSuite(TestDungeon))


if __name__ == '__main__':
    unittest.main()
