import unittest
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
        
    # def test_change_unchangeable(self):
    #     self.assertEqual(self.board.play('A', 2, 4), "You can't change boards default numbers")
    
if __name__ == '__main__':
    unittest.main()
