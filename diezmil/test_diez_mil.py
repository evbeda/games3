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
        self.assertEqual(self.game.check_players_qty(0), False)

    #play testings
    def test_roll_dices_error(self):
        dice_qty = self.play.play_dices(7)
        self.assertEqual(dice_qty, False)

    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_5_dices(self, mock_randint):
        dice_qty = self.play.play_dices(5)
        self.assertEqual(self.play.dices, [1, 1, 1, 1, 1])

    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_3_dices(self, mock_randint):
        dice_qty = self.play.play_dices(3)
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
    # Test is a stair
    @parameterized.expand([
        ([1, 2, 3, 4, 5], True),
        ([1, 3, 2, 5, 4], True),
        ([2, 3, 4, 5, 6], True),
        ([3, 2, 5, 4, 6], True),
        ([1, 1, 3, 4, 2], False),
        ([1, 1, 5, 4, 4], False),
    ])
    def test_is_a_stair(self, dices, expected):
        self.assertEqual(self.play.is_a_stair(dices), expected)

    # Test is a repeated
    @parameterized.expand([
        ([1, 1, 1, 3, 2], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 1, 1], True),
    ])
    def test_is_repeated(self, dices, expected):
        self.assertEqual(self.play.is_repeated(dices), expected)

    # Test calculate repeated
    @parameterized.expand([
        ([2, 3, 3, 4, 4], ([], 0)),  # no score
        ([1, 3, 3, 3, 3], ([3, 3, 3, 3], 600)),  # quadruple
        ([4, 1, 1, 1, 1], ([1, 1, 1, 1], 2000)),  # four_ones
        ([1, 1, 1, 1, 1], ([1, 1, 1, 1, 1], 10000)),  # five_ones
        ([5, 5, 5, 5, 5], ([5, 5, 5, 5, 5], 2000)),  # five_fives
    ])
    def test_calculate_repeated(self, dices, expected_score):
        self.assertEqual(self.play.calculate_repeated(dices), expected_score)

    # Test check combination
    @parameterized.expand([
        ([1, 1, 1, 4, 5], ([1, 1, 1], 1000)),
        ([1, 1, 1, 1, 5], ([1, 1, 1, 1], 2000)),
        ([1, 4, 3, 4, 5], ([], 0)),
        ([3, 3, 3, 4, 5], ([3, 3, 3], 300)),
        ([4, 4, 4, 4, 5], ([4, 4, 4, 4], 800)),
        ([1, 1, 1, 1, 1], ([1, 1, 1, 1, 1], 10000)),
    ])
    def test_check_combination(self, dices, expected_result):
        self.assertEqual(self.play.check_combination(dices), expected_result)


if __name__ == '__main__':
    unittest.main()
