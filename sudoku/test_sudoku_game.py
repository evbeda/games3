import unittest
from parameterized import parameterized
from .game import SudokuGame
from .board import Board


class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()

    def test_initial_next_turn(self):
        self.assertEqual(self.game.next_turn(), 'Place a number')

    def test_game_is_over(self):
        self.game.is_playing = False
        self.assertEqual(self.game.next_turn(), 'Game over')

    @parameterized.expand([
        ('a 1 2',),
        ('b 8 6',),
        ('c 3 8',),
        ('d 4 7',),
        ('e 5 4',),
        ('f 6 8',),
        ('g 7 7',),
        ('h 2 8',),
        ('i 9 6',),
        ('e 1 8',),
        ('g 2 5',),
        ('e 9 1',),
        ('a 5 7',),
    ])
    def test_play_number_legally(self, user_input):
        self.assertEqual(self.game.play(user_input), 'Number added.')

    @parameterized.expand([
        ('a 1 6',),
        ('b 8 2',),
        ('c 3 4',),
        ('d 4 1',),
        ('e 5 5',),
        ('f 6 7',),
        ('g 7 6',),
        ('h 2 5',),
        ('i 9 4',),
        ('e 1 7',),
        ('g 2 3',),
        ('e 9 2',),
        ('a 5 5',),
    ])
    def test_play_number_ilegally(self, user_input):
        self.assertEqual(self.game.play(user_input), 'Invalid number.')

    @parameterized.expand([
        ('a 2 6',),
        ('b 5 9',),
        ('c 9 7',),
        ('d 2 9',),
        ('f 3 3',),
        ('g 8 1',),
        ('h 7 5',),
    ])
    def test_play_number_forbidden(self, user_input):
        self.assertEqual(
            self.game.play(user_input),
            'You can not modify the initial values.')

    def test_play_win(self):
        self.game.game_board = Board(
            " 61375894"
            "537894162"
            "948216357"
            "694751238"
            "825943671"
            "713628945"
            "356482719"
            "489167523"
            "172539486"
        )
        self.assertEqual(self.game.play("a 1 2"), 'You win!')
