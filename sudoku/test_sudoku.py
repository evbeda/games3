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


if __name__ == '__main__':
    unittest.main()
