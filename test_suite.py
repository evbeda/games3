import unittest
from uno.test_uno_cards import TestUnoCards
from uno.test_stack_uno import TestStack
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
from ruleta.test_ruleta import TestRuleta
from sudoku.test_sudoku_board import TestSudokuBoard
from sudoku.test_sudoku_game import TestSudokuGame
from sudoku.test_api import TestSudokuApi
from diezmil.test_diez_mil import TestDiezMil


def suite():
    test_suite = unittest.TestSuite()
    # UNO
    test_suite.addTest(unittest.makeSuite(TestUnoCards))
    test_suite.addTest(unittest.makeSuite(TestStack))
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
    test_suite.addTest(unittest.makeSuite(TestRuleta))
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestSudokuBoard))
    test_suite.addTest(unittest.makeSuite(TestSudokuGame))
    test_suite.addTest(unittest.makeSuite(TestSudokuApi))
    # DIEZ MIL
    test_suite.addTest(unittest.makeSuite(TestDiezMil))
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))


if __name__ == '__main__':
    unittest.main()
