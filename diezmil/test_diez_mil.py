import unittest
from unittest.mock import patch
from .diez_mil import DiezMil
from .play import Play


class TestDiezMil(unittest.TestCase):
    def setUp(self):
        self.game = DiezMil()
        self.play = Play()
        self.game.players_qty = 2
        self.game.baseScore = 450

    def test_check_players_qty(self):
        check_players_qty = self.game.check_players_qty(0)
        self.assertEqual(check_players_qty, False)    

    def test_check_combination_no_score(self):
        dice=[2,3,3,4,4]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 0)
    
    def test_check_combination_score(self):
        dice=[1,3,2,5,3]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 150)

    def test_check_combination_score_triple(self):
        dice=[1,3,3,5,3]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 450)
        
    def test_check_combination_score_quadruple(self):
        dice=[1,3,3,3,3]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 700)
<<<<<<< HEAD
=======
    
    def test_check_combination_score_triple_1(self):
        dice=[1,1,1,5,3]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 1050)
>>>>>>> all test passed

    def test_check_combination_score_flush(self):
        dice=[4,1,2,5,3]
        score=self.play.check_combination(dice)
        self.assertEqual(score, 500)

    #play testings
    def test_roll_dices_error(self):
        dice_qty=self.play.play_dices(7)
        self.assertEqual(dice_qty, False)

    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_5_dices(self, mock_randint):
        dice_qty=self.play.play_dices(5)
        self.assertEqual(self.play.dices, [1, 1, 1, 1, 1])
    
    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_3_dices(self, mock_randint):
        dice_qty=self.play.play_dices(3)
        self.assertEqual(self.play.dices, [1, 1, 1])
    
if __name__ == '__main__':
    unittest.main()
