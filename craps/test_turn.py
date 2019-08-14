import unittest
from unittest.mock import patch
from parameterized import parameterized
from .turn import Turn
from .constants import GAME_IN_PROGRESS, GAME_STARTED, PLAYER_LOST, PLAYER_WON


class TestTurn(unittest.TestCase):
    def setUp(self):
        self.turn = Turn()

    def test_first_state_game_started(self):
        self.assertEqual(self.turn.state, GAME_STARTED)
        self.assertEqual(self.turn.point, None)

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

    @parameterized.expand([((2, 2), 4), ((2, 3), 5), ((4, 2), 6), ((4, 4), 8), ((5, 4), 9), ((5, 5), 10)])
    def test_keep_playing_game(self, dice, new_point):
        turn = Turn()
        with patch('random.sample', return_value=dice):
            turn.shoot()
            self.assertEqual(turn.state, GAME_IN_PROGRESS)
            self.assertEqual(turn.point, new_point) 

    @patch('random.sample', return_value=(2, 2))
    def test_game_point_set(self, sample_mock):
        """Tests that Game state changes to GAME_IN_PROGRESS after first throw (if not winning or losing)."""
        self.turn.shoot()
        self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
        self.assertEqual(self.turn.point, 4)

    @patch('random.sample', return_value=(2, 3))
    def test_point_reached(self, sample_mock):
        self.turn.shoot()
        self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
        self.assertEqual(self.turn.point, 5)
        self.turn.shoot()
        self.assertEqual(self.turn.state, PLAYER_WON)

    def test_point_not_reached_and_lost(self):
        with patch('random.sample', return_value=(2, 3)):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, 5)
        with patch('random.sample', return_value=(2, 4)):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, 5)
        with patch('random.sample', return_value=(2, 5)):
            self.turn.shoot()
            self.assertEqual(self.turn.state, PLAYER_LOST)

    def test_point_not_reached_and_won(self):
        FIRST_DICE = (2, 3)
        POINT = sum(FIRST_DICE)
        with patch('random.sample', return_value=FIRST_DICE):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, POINT)
        with patch('random.sample', return_value=(2, 4)):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, POINT)
        with patch('random.sample', return_value=FIRST_DICE):
            self.turn.shoot()
            self.assertEqual(self.turn.state, PLAYER_WON)


if __name__ == '__main__':
    unittest.main(verbosity=2)
