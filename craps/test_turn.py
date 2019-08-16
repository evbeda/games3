import unittest
from unittest.mock import patch
from parameterized import parameterized
from .bet import PassBet, DoNotPassBet
from .turn import Turn
from .constants import GAME_IN_PROGRESS, GAME_STARTED, PLAYER_LOST, PLAYER_WON


class TestTurn(unittest.TestCase):
    def setUp(self):
        self.turn = Turn()

    def test_first_state_game_started(self):
        self.assertEqual(self.turn.state, GAME_STARTED)
        self.assertEqual(self.turn.point, None)

    def test_shoots_two_dice(self):
        # Tests that only two dice are thrown.
        dice = self.turn.shoot()
        dice_count = len(dice)
        self.assertEqual(dice_count, 2)

    def test_dice_shot_numbers(self):
        # Tests that dice numbers are between 1 and 6.
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

    @parameterized.expand([
        ((2, 2), 4),
        ((2, 3), 5),
        ((4, 2), 6),
        ((4, 4), 8),
        ((5, 4), 9),
        ((5, 5), 10)
    ])
    def test_keep_playing_game(self, dice, new_point):
        turn = Turn()
        with patch('random.sample', return_value=dice):
            turn.shoot()
            self.assertEqual(turn.state, GAME_IN_PROGRESS)
            self.assertEqual(turn.point, new_point)

    @patch('random.sample', return_value=(2, 2))
    def test_game_point_set(self, _sample_mock):
        # Tests that Game state changes to GAME_IN_PROGRESS after first
        # throw (if not winning or losing).
        self.turn.shoot()
        self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
        self.assertEqual(self.turn.point, 4)

    @patch('random.sample', return_value=(2, 3))
    def test_point_reached(self, _sample_mock):
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
        first_dice = (2, 3)
        point = sum(first_dice)
        with patch('random.sample', return_value=first_dice):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, point)
        with patch('random.sample', return_value=(2, 4)):
            self.turn.shoot()
            self.assertEqual(self.turn.state, GAME_IN_PROGRESS)
            self.assertEqual(self.turn.point, point)
        with patch('random.sample', return_value=first_dice):
            self.turn.shoot()
            self.assertEqual(self.turn.state, PLAYER_WON)

    def _set_bets(self):
        bet1 = PassBet(5)
        bet2 = DoNotPassBet(8)
        bet3 = DoNotPassBet(15)
        bet4 = PassBet(2)
        self.turn.bets = [bet1, bet2, bet3, bet4]

    # REFACTOR

    @parameterized.expand([
        (PLAYER_WON, [0, 3]),   # Activate PASS_BETS
        (PLAYER_LOST, [1, 2])   # Activate DO_NOT_PASS_BETS
    ])
    def test_check_bets_get_activated(self, state, expected_bets_index):
        self._set_bets()
        self.turn.state = state
        expected_activated_bets = []
        for index in expected_bets_index:
            expected_activated_bets.append(self.turn.bets[index])
        actual_activated_bets = self.turn.check_bets((5, 5))
        self.assertEqual(actual_activated_bets, expected_activated_bets)

    @parameterized.expand([
        (PLAYER_WON, [1, 2]),   # Only remains DO_NOT_PASS_BETS
        (PLAYER_LOST, [0, 3])   # Only remains PASS_BETS
    ])
    def test_check_bets_get_deleted(self, state, expect_remaining_bets_index):
        self._set_bets()
        self.turn.state = state
        expected_remaining_bets = []
        for index in expect_remaining_bets_index:
            expected_remaining_bets.append(self.turn.bets[index])
        self.turn.check_bets((5, 5))
        actual_remaining_bets = self.turn.bets
        self.assertEqual(actual_remaining_bets, expected_remaining_bets)

    @parameterized.expand([
        (PLAYER_WON, 7*2),      # win PASS_BETS
        (PLAYER_LOST, 23*2)     # win DO_NOT_PASS_BETS
    ])
    def test_pay_bets(self, state, expected_payment):
        self._set_bets()
        self.turn.state = state
        payment = self.turn.pay_bets((5, 5))
        self.assertEqual(payment, expected_payment)
    # END REFACTOR
