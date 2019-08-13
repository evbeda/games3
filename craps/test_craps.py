"""Tests para la clase Game"""
import unittest
from game import Game
from constants import GAME_STARTED


class TestCraps(unittest.TestCase):
    def test_game_initial_state_(self):
        game = Game()
        self.assertEqual(game.state, GAME_STARTED)


if __name__ == '__main__':
    unittest.main(verbosity=2)
