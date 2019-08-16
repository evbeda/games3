import unittest
from parameterized import parameterized
from .game import SudokuGame
from .board import Board
from .api import mocked_requests_get
from . import (
    NUMBER_ADDED,
    YOU_WIN,
    GAME_OVER,
    PLACE_A_NUMBER,
    NOT_MODIFIABLE,
    REPEATED_ON_COLUMN,
    REPEATED_ON_ROW,
    REPEATED_ON_REGION,
    EXAMPLE_BOARD,
    API_BOARD,
)


class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame(EXAMPLE_BOARD)

    def test_initial_next_turn(self):
        self.assertEqual(self.game.next_turn(), PLACE_A_NUMBER)

    def test_game_is_over(self):
        self.game.is_playing = False
        self.assertEqual(self.game.next_turn(), GAME_OVER)

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
        self.assertEqual(self.game.play(user_input), NUMBER_ADDED)

    @parameterized.expand([
        ('a 1 6', REPEATED_ON_ROW),
        ('b 8 2', REPEATED_ON_COLUMN),
        ('c 3 2', REPEATED_ON_COLUMN),
        ('d 4 1', REPEATED_ON_ROW),
        ('B 7 4', REPEATED_ON_REGION),
    ])
    def test_play_number_ilegally(self, user_input, message):
        self.assertIn(message, self.game.play(user_input))

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
        self.assertIn(NOT_MODIFIABLE, self.game.play(user_input))

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
        self.assertEqual(self.game.play("a 1 2"), YOU_WIN)

    def test_play_with_specific_board(self):
        game = SudokuGame(EXAMPLE_BOARD)
        self.assertEqual(game.game_board.board, Board(EXAMPLE_BOARD).board)

    @unittest.mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_play_with_fetched_board(self, mocked_requests_get):
        game = SudokuGame()
        self.assertEqual(game.game_board.board, Board(API_BOARD).board)

    def test_board(self):
        expected = "  6   |3     |8   4 \n" \
            "5 3 7 |  9   |      \n" \
            "  4   |    6 |3   7 \n" \
            "------+------+------\n" \
            "  9   |  5 1 |2 3 8 \n" \
            "      |      |      \n" \
            "7 1 3 |6 2   |  4   \n" \
            "------+------+------\n" \
            "3   6 |4     |  1   \n" \
            "      |  6   |5 2 3 \n" \
            "1   2 |    9 |  8   \n"
        self.assertEqual(expected, self.game.board)
