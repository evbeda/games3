import unittest
from uno.test_uno_cards import TestUnoCards
from uno.test_stack_uno import TestStack
from uno.test_uno_game import TestUnoGame
from uno.test_uno_player import TestPlayerUno
from craps.test_craps import TestCraps
from craps.test_turn import TestTurn
from craps.test_bets import TestBets
from dungeon_raiders.tests.test_suite_dungeon import suite as dr_suite
from sudoku.tests.test_suite_sudoku import suite as sudoku_suite
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from ruleta.tests.test_ruleta import (
    TestRoulette,
    TestBoard
)
from ruleta.tests.test_bets import (
    TestBetsRoulette,
    TestBetCreator,
)
from ruleta.tests.test_croupier import TestCroupier
from ruleta.tests.integration_test import IntegrationTest
from diezmil.test_diez_mil import TestDiezMil
from test_game import TestGame


def suite():
    test_suite = unittest.TestSuite()
    # UNO
    test_suite.addTest(unittest.makeSuite(TestUnoCards))
    test_suite.addTest(unittest.makeSuite(TestStack))
    test_suite.addTest(unittest.makeSuite(TestUnoGame))
    test_suite.addTest(unittest.makeSuite(TestPlayerUno))
    # CRAPS
    test_suite.addTest(unittest.makeSuite(TestCraps))
    test_suite.addTest(unittest.makeSuite(TestTurn))
    test_suite.addTest(unittest.makeSuite(TestBets))
    # ROULETTE
    test_suite.addTest(unittest.makeSuite(TestBetsRoulette))
    test_suite.addTest(unittest.makeSuite(TestBetCreator))
    test_suite.addTest(unittest.makeSuite(TestRoulette))
    test_suite.addTest(unittest.makeSuite(TestCroupier))
    test_suite.addTest(unittest.makeSuite(IntegrationTest))
    test_suite.addTest(unittest.makeSuite(TestBoard))
    # SUDOKU
    # test_suite.addTest(unittest.makeSuite(TestSudokuBoard))
    # test_suite.addTest(unittest.makeSuite(TestSudokuGame))
    # test_suite.addTest(unittest.makeSuite(TestSudokuApi))
    # DIEZ MIL
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    # GAME MACHINE
    test_suite.addTest(unittest.makeSuite(TestGame))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    alltests.addTest(dr_suite())
    alltests.addTest(sudoku_suite())
    unittest.TextTestRunner().run(alltests)
