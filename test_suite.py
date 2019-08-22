import unittest
from uno.uno_suite import suite as uno_suite
from craps.craps_suite import suite as craps_suite
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
    test_suite.addTest(uno_suite())
    # CRAPS
    test_suite.addTest(craps_suite())
    # ROULETTE
    test_suite.addTest(unittest.makeSuite(TestBetsRoulette))
    test_suite.addTest(unittest.makeSuite(TestBetCreator))
    test_suite.addTest(unittest.makeSuite(TestRoulette))
    test_suite.addTest(unittest.makeSuite(TestCroupier))
    test_suite.addTest(unittest.makeSuite(IntegrationTest))
    test_suite.addTest(unittest.makeSuite(TestBoard))
    # SUDOKU
    test_suite.addTest(sudoku_suite())
    # DANGEONS RAIDERS
    test_suite.addTest(dr_suite())
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
    unittest.TextTestRunner().run(alltests)
