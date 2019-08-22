import unittest
from .test_stack_uno import TestStack
from .test_uno_cards import TestUnoCards
from .test_uno_game import TestUnoGame
from .test_uno_player import TestPlayerUno


def suite():
    test_suite = unittest.TestSuite()
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestStack))
    test_suite.addTest(unittest.makeSuite(TestUnoCards))
    test_suite.addTest(unittest.makeSuite(TestUnoGame))
    test_suite.addTest(unittest.makeSuite(TestPlayerUno))
    return test_suite
