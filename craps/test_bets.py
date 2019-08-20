import unittest
from parameterized import parameterized
from .turn import Turn
from .bet import Bet, BetCreator, PassBet, DoNotPassBet, SevenBet, DoubleBet
from .game import CrapsGame
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_IN_PROGRESS,
    GAME_STARTED,
    BET_IN_PROGRESS,
    BET_LOST,
    BET_PAYED,
)

BET_SCENARIO = [
        (PassBet(10, None), PLAYER_WON, (1, 1), True, 20),
        (PassBet(20, None), PLAYER_LOST, (1, 1), False, 0),
        (PassBet(30, None), GAME_IN_PROGRESS, (1, 1), False, 0),
        (PassBet(40, None), GAME_STARTED, (1, 1), False, 0),
        (DoNotPassBet(10, None), PLAYER_LOST, (1, 6), True, 20),
        (DoNotPassBet(20, None), PLAYER_WON, (1, 1), False, 0),
        (DoNotPassBet(30, None), GAME_IN_PROGRESS, (1, 1), False, 0),
        (DoNotPassBet(40, None), GAME_STARTED, (1, 1), False, 0),
        (DoubleBet(10, None), PLAYER_LOST, (1, 1), True, 300),
        (DoubleBet(20, None), PLAYER_WON, (2, 2), True, 160),
        (DoubleBet(30, None), GAME_IN_PROGRESS, (3, 3), True, 300),
        (DoubleBet(40, None), GAME_STARTED, (4, 3), False, 0),
        (SevenBet(40, None), GAME_STARTED, (4, 3), True, 160),
        (SevenBet(40, None), GAME_STARTED, (4, 4), False, 0),
    ]


class TestBets(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_not_possible_to_check_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10, None).check(self.game.turn)

    def test_not_possible_to_pay_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10, None).pay(self.game.turn)

    @parameterized.expand([
        ("PASS_BET", PassBet),
        ("DO_NOT_PASS_BET", DoNotPassBet),
        ("DOUBLE_BET", DoubleBet),
        ("SEVEN_BET", SevenBet)
    ])
    def test_bet_creator_returns_correct_type(self, type_string, bet_child):
        turn = Turn()
        bet = BetCreator.create(type_string, 2, (1, 2), turn)
        self.assertIsInstance(bet, bet_child)

    def test_bet_creator_raises_invalid_type_exception(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.create("sadkjagskjdg", 2, (1, 2))

    @parameterized.expand(BET_SCENARIO)
    def test_bet_check_true(self, bet, state, dice,
                            result, _expected_payment):
        turn = self.game.turn
        turn.state = state
        turn.dice = dice
        self.assertEqual(bet.check(turn), result)

    @parameterized.expand(BET_SCENARIO)
    def test_bet_pay(self, bet, state, dice, _result, expected_payment):
        turn = self.game.turn
        turn.state = state
        turn.dice = dice
        self.assertEqual(bet.pay(turn), expected_payment)

    def test_bet_states_in_progress_initial_state(self):
        turn = Turn()
        bet = BetCreator.create("PASS_BET", 20, turn)
        self.assertEqual(bet.state, BET_IN_PROGRESS)

    @parameterized.expand([
        (PassBet(10, None), PLAYER_WON, (2, 5), BET_PAYED),
        (PassBet(10, None), PLAYER_LOST, (6, 6), BET_LOST),
        (PassBet(10, None), PLAYER_WON, (5, 2), BET_PAYED),
        (PassBet(10, None), PLAYER_LOST, (5, 3), BET_LOST)
        ])
    def test_bet_states_payed(self, bet, turn_state, dice, bet_state):
        turn = self.game.turn
        turn.state = turn_state
        turn.dice = dice
        bet.pay(turn)
        self.assertEqual(bet.state, bet_state)
