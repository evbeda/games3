import unittest
# from game import Game
from board import Board

class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        self.assertTrue(True)
    
    def test_present_numbers_unchangeable(self):
        self.assertTrue(self.board.unchangeable('A', 3))
        
    # def test_change_unchangeable(self):
    #     self.assertEqual(self.board.play('A', 2, 4), "You can't change boards default numbers")
    
if __name__ == '__main__':
    unittest.main()
