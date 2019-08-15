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

    @parameterized.expand([
        ([1, 5, 5], 200),
        ([1, 5], 150),
        ([1, 5, 1, 2, 3], 250),
        ([2, 3, 2], 0),
        ([5], 50),
    ])
    def test_individual_values(self, dices, expected_score):
        score = self.play.calculate_individual_values(dices)
        self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()
