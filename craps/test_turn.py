import unittest
from unittest.mock import patch
from turn import Turn
from constants import GAME_IN_PROGRESS, GAME_STARTED, PLAYER_LOST, PLAYER_WON


class TestTurn(unittest.TestCase):
    def setUp(self):
        self.turn = Turn()

    def test_shoots_two_dice(self):
        """Tests that only two dice are thrown."""
        dice = self.turn.shoot()
        dice_count = len(dice)
        self.assertEqual(dice_count, 2)

    def test_dice_shot_numbers(self):
        """Tests that dice numbers are between 1 and 6."""
        dice = self.turn.shoot()
        for die in dice:
            self.assertGreaterEqual(die, 1)
            self.assertLessEqual(die, 6)

    def test_player_loses_on_first_throw(self):
        losing_dice = [(1, 2), (1, 1), (6, 6)]
        for dice in losing_dice:
            self.assertEqual(self.turn.get_next_state(dice), PLAYER_LOST)

    def test_player_wins_on_first_throw(self):
        winning_dice = [(4, 3), (5, 2), (6, 1), (5, 6)]
        for dice in winning_dice:
            self.assertEqual(self.turn.get_next_state(dice), PLAYER_WON)

    @patch('random.sample')
    def test_game_state_changes_when_throw(self, sample_mock):
        """Tests that Game state changes to GAME_IN_PROGRESS after first throw (if not winning or losing)."""
        sample_mock.return_value = (2, 2)
        self.turn.shoot()
        self.assertEqual(self.turn.state, GAME_IN_PROGRESS)


if __name__ == '__main__':
    unittest.main(verbosity=2)
