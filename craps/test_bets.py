import unittest
from parameterized import parameterized
from .bet import BetCreator, PassBet, DoNotPassBet
from .game import CrapsGame
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
# from .constants import (
#     PLAYER_LOST,
#     PLAYER_WON,
#     GAME_STARTED,
#     GAME_IN_PROGRESS,
#     WON_MESSAGE,
#     LOST_MESSAGE,
#     BET_MESSAGE,
# )


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
