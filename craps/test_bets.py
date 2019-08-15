import unittest
from parameterized import parameterized
from .bet import Bet, BetCreator, PassBet, DoNotPassBet
from .game import CrapsGame
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_IN_PROGRESS,
    GAME_STARTED
)

BET_SCENARIO = [
        (PassBet(10), PLAYER_WON, (1, 1), True, 20),
        (PassBet(20), PLAYER_LOST, (1, 1), False, 40),
        (PassBet(30), GAME_IN_PROGRESS, (1, 1), False, 60),
        (PassBet(40), GAME_STARTED, (1, 1), False, 80),
        (DoNotPassBet(10), PLAYER_LOST, (1, 6), True, 20),
        (DoNotPassBet(20), PLAYER_WON, (1, 1), False, 40),
        (DoNotPassBet(30), GAME_IN_PROGRESS, (1, 1), False, 60),
        (DoNotPassBet(40), GAME_STARTED, (1, 1), False, 80)
    ]


class TestBets(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_not_possible_to_check_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10).check(self.game.turn, (1, 1))

    def test_not_possible_to_pay_in_parent_bet(self):
        with self.assertRaises(NotImplementedError):
            Bet(10).pay()

    @parameterized.expand([
        ("PASS_BET", PassBet),
        ("DO_NOT_PASS_BET", DoNotPassBet)
    ])
    def test_bet_creator_returns_correct_type(self, type_string, result):
        bet = BetCreator.create(type_string, 2)
        self.assertIsInstance(bet, result)

    def test_bet_creator_raises_invalid_type_exception(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.create("sadkjagskjdg", 2)

    @parameterized.expand(BET_SCENARIO)
    def test_bet_check_true(self, bet, state, dice, result, *args):
        self.game.turn.state = state
        self.assertEqual(bet.check(self.game.turn, dice), result)

    @parameterized.expand(BET_SCENARIO)
    def test_bet_payment(self, bet, _state, _dice, _result, expected_payment):
        self.assertEqual(bet.pay(), expected_payment)
