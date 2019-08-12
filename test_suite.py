import unittest
from uno.test_uno import TestUno
from craps.test_craps import TestCraps
from dungeon_raiders.test_dungeon import TestDungeon
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from ruleta.test_ruleta import TestRuleta
from sudoku.test_sudoku import TestSudoku
from diezmil.test_diez_mil import TestDiezMil


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUno))
    test_suite.addTest(unittest.makeSuite(TestCraps))
    test_suite.addTest(unittest.makeSuite(TestDungeon))
    test_suite.addTest(unittest.makeSuite(TestRuleta))
    test_suite.addTest(unittest.makeSuite(TestSudoku))
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))


if __name__ == '__main__':
    unittest.main()
