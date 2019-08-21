import unittest
from parameterized import parameterized
from unittest.mock import patch
from .bet import PassBet
from .game import CrapsGame
from .turn import Turn
from .bet import BetCreator
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_OVER,
    GAME_STARTED,
    GAME_IN_PROGRESS,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE,
    OUT_OF_CASH,
    CAN_NOT_LEAVE,
    PASS_BET,
    DO_NOT_PASS_BET,
    GO_COMMAND,
    NO_COMMAND,
    BET_AGAIN_OR_GO,
    SHOOT_DICE_MESSAGE,
)


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.game = CrapsGame()

    @parameterized.expand([
        (GAME_STARTED, [], [], "Point: None\nDice: None\nMoney: 1000"),
        (GAME_STARTED, ['PASS_BET', 20, None], [], "Point: None\nDice: None\nBet:\nBet type: PassBet\nAmount bet: 20\nAmount payed: 0\nBet state: Bet in progress\nMoney: 980"),
        (GAME_IN_PROGRESS, ['PASS_BET', 20, None], (6, 3), "Point: 9\nDice: (6, 3)\nBet:\nBet type: PassBet\nAmount bet: 20\nAmount payed: 0\nBet state: Bet in progress\nMoney: 980"),
    ])
    def test_show_board(self, state, bets, dice, expected):
        self.game.turn.state = state
        if bets:
            bet = BetCreator.create(bets[0], bets[1], self.game.turn, bets[2])
            self.game.decrease_money(bets[1])
            self.game.turn.bets.append(bet)
        if dice:
            with patch('random.sample', return_value=dice):
                self.game.play(GO_COMMAND)
        boards = self.game.board
        self.assertEqual(boards, expected)
