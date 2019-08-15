import unittest
from uno.test_uno import TestUno
from craps.test_craps import TestCraps
from craps.test_turn import TestTurn
from craps.test_bets import TestBets
from dungeon_raiders.test_dungeon import TestDungeon
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from ruleta.test_ruleta import TestRuleta
from sudoku.test_sudoku import TestSudoku
from diezmil.test_diez_mil import TestDiezMil


def suite():
    test_suite = unittest.TestSuite()
    # UNO
    test_suite.addTest(unittest.makeSuite(TestUno))
    # CRAPS
    test_suite.addTest(unittest.makeSuite(TestCraps))
    test_suite.addTest(unittest.makeSuite(TestTurn))
    test_suite.addTest(unittest.makeSuite(TestBets))
    # DUNGEON RAIDERS
    test_suite.addTest(unittest.makeSuite(TestDungeon))
    # ROULETTE
    test_suite.addTest(unittest.makeSuite(TestRuleta))
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestSudoku))
    # DIEZ MIL
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))


if __name__ == '__main__':
    unittest.main()
