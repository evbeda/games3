import unittest
from parameterized import parameterized
from .bet import Bet, BetCreator, PassBet, DoNotPassBet, DoubleBet
from .game import CrapsGame
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_IN_PROGRESS,
    GAME_STARTED
)

BET_SCENARIO = [
        (PassBet(10, (1, 1)), PLAYER_WON, (1, 1), True, 20),
        (PassBet(20, (1, 1)), PLAYER_LOST, (1, 1), False, 0),
        (PassBet(30, (1, 1)), GAME_IN_PROGRESS, (1, 1), False, 0),
        (PassBet(40, (1, 1)), GAME_STARTED, (1, 1), False, 0),
        (DoNotPassBet(10, (1, 1)), PLAYER_LOST, (1, 6), True, 20),
        (DoNotPassBet(20, (1, 1)), PLAYER_WON, (1, 1), False, 0),
        (DoNotPassBet(30, (1, 1)), GAME_IN_PROGRESS, (1, 1), False, 0),
        (DoNotPassBet(40, (1, 1)), GAME_STARTED, (1, 1), False, 0),
        (DoubleBet(10, (1, 1)), PLAYER_LOST, (1, 1), True, 300),
        (DoubleBet(20, (2, 2)), PLAYER_WON, (2, 2), True, 160),
        (DoubleBet(30, (3, 3)), GAME_IN_PROGRESS, (3, 3), True, 300),
        (DoubleBet(40, (4, 4)), GAME_STARTED, (4, 3), False, 0),
    ]


class TestBets(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_not_possible_to_check_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10).check(self.game.turn)

    def test_not_possible_to_pay_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10).pay(self.game.turn)

    @parameterized.expand([
        ("PASS_BET", PassBet),
        ("DO_NOT_PASS_BET", DoNotPassBet),
        ("DOUBLE_BET", DoubleBet)
    ])
    def test_bet_creator_returns_correct_type(self, type_string, bet_child):
        bet = BetCreator.create(type_string, 2, (1, 2))
        self.assertIsInstance(bet, bet_child)

    def test_bet_creator_raises_invalid_type_exception(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.create("sadkjagskjdg", 2, (1, 2))

    @parameterized.expand(BET_SCENARIO)
    def test_bet_check_true(self, bet, state, dice, result, *args):
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
