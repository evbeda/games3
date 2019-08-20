import unittest
from unittest.mock import patch
from parameterized import parameterized
from .exceptions.out_of_cash_exception import OutOfCashException
from .game import CrapsGame
from .turn import Turn
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_STARTED,
    GAME_IN_PROGRESS,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE,
    OUT_OF_CASH,
    CAN_NOT_LEAVE,
)


class TestCraps(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_craps_game_started(self):
        self.assertTrue(self.game.is_playing)
        self.assertIsInstance(self.game.turn, Turn)

    def test_craps_game_started_asks_for_a_bet(self):
        self.assertEqual(self.game.turn.state, GAME_STARTED)
        self.assertEqual(self.game.next_turn(), BET_MESSAGE)

    def test_craps_game_in_progress_asks_for_a_bet(self):
        self.game.turn.state = GAME_IN_PROGRESS
        self.assertEqual(self.game.next_turn(), BET_MESSAGE)

    def test_craps_player_lost_aks_keep_playing(self):
        self.game.turn.state = PLAYER_LOST
        self.assertEqual(self.game.next_turn(), LOST_MESSAGE)

    def test_craps_player_won_aks_keep_playing(self):
        self.game.turn.state = PLAYER_WON
        self.assertEqual(self.game.next_turn(), WON_MESSAGE)

    @parameterized.expand([
        (PLAYER_WON, ),
        (PLAYER_LOST, ),
    ])
    def test_craps_player_wants_to_quit_allowed(self, state):
        self.game.turn.state = state
        self.assertEqual(self.game.play('No'), 'Game Over')

    def test_craps_player_wants_to_quit_not_allowed(self):
        self.game.turn.state = GAME_IN_PROGRESS
        self.assertEqual(self.game.play('No'), CAN_NOT_LEAVE + BET_MESSAGE)

    @parameterized.expand([
        ((2, 2),),
        ((2, 3),),
        ((4, 2),),
        ((4, 4),),
        ((5, 4),),
        ((5, 5),),
    ])
    def test_craps_play_returns_score(self, dice):
        with patch('random.sample', return_value=dice):
            self.assertEqual(self.game.play('Go'), dice)

    @parameterized.expand([
        ("PASS_BET 10", ("PASS_BET", 10, [])),
        ("PASS_BET 100 5", ("PASS_BET", 100, [5])),
        ("DO_NOT_PASS_BET 10 2 4", ("DO_NOT_PASS_BET", 10, [2, 4])),
        ("PASS_BET 10 3 4 1 5", ("PASS_BET", 10, [3, 4]))
    ])
    def test_craps_game_input_commands(self, input, result):
        self.assertEqual(self.game.resolve_command(input), result)

    def test_craps_game_input_bet_placed_message(self):
        returned_play = self.game.play("PASS_BET", 10)
        self.assertEqual(returned_play, BET_PLACED + "PASS_BET")

    def test_craps_game_bet_added_to_bets_list(self):
        # self.game.play("PASS_BET 10")
        # self.game.play("DO_NOT_PASS_BET 20")
        self.game.play("PASS_BET", 10)
        self.game.play("DO_NOT_PASS_BET", 20)
        self.assertEqual(len(self.game.turn.bets), 2)

    def test_craps_game_invalid_bet_type(self):
        # returned_play = self.game.play("INVALIDBET 5678")
        returned_play = self.game.play("INVALIDBET", 5678)
        self.assertEqual(returned_play, INVALID_BET_TYPE)

    def test_craps_not_enough_cash(self):
        returned_play = self.game.play("PASS_BET", 9999999)
        self.assertEqual(returned_play, OUT_OF_CASH)

    def test_craps_play_decrase_money(self):
        self.game.play("DO_NOT_PASS_BET", 300)
        self.assertEqual(self.game.money, 700)

    def test_craps_decrease_money(self):
        self.game.decrease_money(200)
        self.assertEqual(self.game.money, 800)

    def test_craps_decrease_money_exception(self):
        with self.assertRaises(OutOfCashException):
            self.game.decrease_money(1200)

    @patch('random.sample', return_value=(1, 1))
    def test_craps_pay_bets_give_money(self, _):
        # bets 50 on winning and 100 on losing
        # 850 money remaining
        # loses (because of the patch), so wins 200
        # 1050 money remaining
        expected_money = 1050
        self.game.play("PASS_BET", 50)
        self.game.play("DO_NOT_PASS_BET", 100)
        self.game.play("Go")
        self.assertEqual(self.game.money, expected_money)

    @parameterized.expand([
        (PLAYER_WON, False),
        (PLAYER_LOST, False),
        (GAME_IN_PROGRESS, True)
    ])
    def test_craps_compare_turn_after_state(self, state, expected):
        self.game.turn.state = state
        first_turn = self.game.turn
        self.game.play('Go')
        is_same_turn = self.game.turn == first_turn
        self.assertEqual(is_same_turn, expected)
