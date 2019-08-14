import unittest
from parameterized import parameterized
# from game import Game
from .board import Board


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.board = Board(
            " 6 3  8 4"
            "537 9    "
            " 4   63 7"
            " 9  51238"
            "         "
            "71362  4 "
            "3 64   1 "
            "    6 523"
            "1 2  9 8 "
        )

    def test_sudoku(self):
        self.assertTrue(True)

    def test_existing_numbers_are_not_modifiable(self):
        self.assertFalse(self.board.is_modifiable('A', 2))

    @parameterized.expand([
        ('a', 3),
        ('b', 7),
        ('c', 6),
        ('d', 5),
        ('f', 1),
        ('g', 4),
        ('h', 2),
        ('i', 9)
    ])
    def test_validate_insert_illegal_value_in_row(self, row, value):
        self.assertFalse(self.board.validate_row(row, value))

    @parameterized.expand([
        ('a', 1),
        ('b', 2),
        ('c', 5),
        ('d', 4),
        ('e', 3),
        ('f', 8),
        ('g', 7),
        ('h', 9),
        ('i', 6)
    ])
    def test_validate_insert_legal_value_in_row(self, row, value):
        self.assertTrue(self.board.validate_row(row, value))

    @parameterized.expand([
        (1, 1),
        (2, 3),
        (3, 2),
        (4, 6),
        (5, 9),
        (6, 6),
        (7, 8),
        (8, 4),
        (9, 7)
    ])
    def test_validate_insert_illegal_value_in_column(self, column, value):
        self.assertFalse(self.board.validate_column(column, value))

    @parameterized.expand([
        (1, 9),
        (2, 8),
        (3, 5),
        (4, 7),
        (5, 4),
        (6, 3),
        (7, 6),
        (8, 5),
        (9, 1)
    ])
    def test_validate_insert_legal_value_in_column(self, column, value):
        self.assertTrue(self.board.validate_column(column, value))

    @parameterized.expand([
        (('a', 1), 9),
        (('b', 4), '1'),
        (('h', 1), 4),
    ])
    def test_place_number_legally(self, coordinates, value):
        row, column = coordinates
        self.board.place(coordinates, value)
        self.assertEqual(self.board.board[row][column - 1]['val'], str(value))
