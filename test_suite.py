import unittest
from uno.test_uno_cards import TestUnoCards
from uno.test_stack_uno import TestStack
from uno.test_uno_game import TestUnoGame
from uno.test_uno_player import TestPlayerUno
from craps.test_craps import TestCraps
from craps.test_turn import TestTurn
from craps.test_bets import TestBets
from dungeon_raiders.test_dungeon import TestDungeon
from dungeon_raiders.test_dungeon import TestMonsterRoom
from dungeon_raiders.test_dungeon import TestTrapRoom
from dungeon_raiders.test_dungeon import TestTreasure
from dungeon_raiders.test_dungeon import TestLevel
from dungeon_raiders.test_dungeon import TestPlayer
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
from sudoku.test_sudoku_board import TestSudokuBoard
from sudoku.test_sudoku_game import TestSudokuGame
from sudoku.test_api import TestSudokuApi
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
    # DUNGEON RAIDERS
    test_suite.addTest(unittest.makeSuite(TestDungeon))
    test_suite.addTest(unittest.makeSuite(TestMonsterRoom))
    test_suite.addTest(unittest.makeSuite(TestTrapRoom))
    test_suite.addTest(unittest.makeSuite(TestTreasure))
    test_suite.addTest(unittest.makeSuite(TestLevel))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    # ROULETTE
    test_suite.addTest(unittest.makeSuite(TestBetsRoulette))
    test_suite.addTest(unittest.makeSuite(TestBetCreator))
    test_suite.addTest(unittest.makeSuite(TestRoulette))
    test_suite.addTest(unittest.makeSuite(TestCroupier))
    test_suite.addTest(unittest.makeSuite(IntegrationTest))
    test_suite.addTest(unittest.makeSuite(TestBoard))
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestSudokuBoard))
    test_suite.addTest(unittest.makeSuite(TestSudokuGame))
    test_suite.addTest(unittest.makeSuite(TestSudokuApi))
    # DIEZ MIL
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    # GAME MACHINE
    test_suite.addTest(unittest.makeSuite(TestGame))


if __name__ == '__main__':
    unittest.main()
