import unittest
from uno.uno_suite import suite as uno_suite
from craps.craps_suite import suite as craps_suite
from dungeon_raiders.tests.test_suite_dungeon import suite as dr_suite
from sudoku.tests.test_suite_sudoku import suite as sudoku_suite
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from diezmil.test_diezmil_suite import suite as diez_mil_suite
from ruleta.tests.test_roulette_suite import suite as roulette_suite
from test_game import TestGame


def suite():
    test_suite = unittest.TestSuite()
    # UNO
    test_suite.addTest(uno_suite())
    # CRAPS
    test_suite.addTest(craps_suite())
    # ROULETTE
    test_suite.addTest(roulette_suite())
    # SUDOKU
    test_suite.addTest(sudoku_suite())
    # DANGEONS RAIDERS
    test_suite.addTest(dr_suite())
    # DIEZ MIL
    test_suite.addTest(diez_mil_suite())
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    # GAME MACHINE
    test_suite.addTest(unittest.makeSuite(TestGame))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
