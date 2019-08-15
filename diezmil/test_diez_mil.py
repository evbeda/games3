import unittest
from unittest.mock import patch
from parameterized import parameterized
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

    @parameterized.expand([
        ([2, 3, 3, 4, 4], 0),  # no score
        ([1, 3, 2, 5, 3], 150),  # simple
        ([1, 3, 3, 5, 3], 450),  # triple
        ([1, 3, 3, 3, 3], 700),  # quadruple
        ([4, 1, 2, 5, 3], 500),  # flush
        ([4, 6, 2, 5, 3], 500),  # flush
        ([4, 1, 2, 1, 1], 1000),  # three_ones
        ([4, 1, 1, 1, 1], 2000),  # four_ones
        ([1, 1, 1, 1, 1], 10000),  # five_ones
        ([5, 5, 5, 5, 5], 2000),  # five_fives
    ])
    def test_check_combination_score(self, dice, expected_score):
        score = self.play.check_combination(dice)
        self.assertEqual(score, expected_score)

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
