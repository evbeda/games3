import unittest
from parameterized import parameterized
from .bet import BetCreator, PassBet, DoNotPassBet
from .game import CrapsGame
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_IN_PROGRESS,
    GAME_STARTED
)


class TestBets(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

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

    @parameterized.expand([
        (PassBet(10), PLAYER_WON, (1, 1), True),
        (PassBet(10), PLAYER_LOST, (1, 1), False),
        (PassBet(10), GAME_IN_PROGRESS, (1, 1), False),
        (PassBet(10), GAME_STARTED, (1, 1), False),
        (DoNotPassBet(10), PLAYER_LOST, (1, 6), True),
        (DoNotPassBet(10), PLAYER_WON, (1, 1), False),
        (DoNotPassBet(10), GAME_IN_PROGRESS, (1, 1), False),
        (DoNotPassBet(10), GAME_STARTED, (1, 1), False)
    ])
    def test_bet_check_true(self, bet, state, dice, result):
        self.game.turn.state = state
        self.assertEqual(bet.check(self.game.turn, dice), result)
