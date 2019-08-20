# Modules
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
# Model
from ..player import Player
from ..croupier import Croupier
from ..game_roullete import GameRoulette
from ..bet import (
    StraightBet,
    ColorBet,
    EvenOddBet,
    LowHighBet,
    StreetBet,
    SixLineBet,
    DoubleBet,
)
# Exceptions
# Messages
from .. import (
    SUCCESS_MESSAGE,
    NOT_ENOUGH_CASH_MESSAGE,
    INVALID_BET_MESSAGE,
    INVALID_BET_TYPE_MESSAGE,
    BYE_MESSAGE,
    END_GAME_COMMAND,
    GO_COMMAND,
    WON_MESSAGE,
    LOST_MESSAGE
)


class IntegrationTest(TestCase):
    # Test for the game roullete
    def setUp(self):
        self.player = Player(100)
        self.croupier = Croupier(self.player)
        self.game = GameRoulette()

    def test_resolve_command_method(self):
        result = self.game.resolve_command('STRAIGHT_BET 14 100')
        self.assertEqual(('STRAIGHT_BET', [14], 100), result)

    @parameterized.expand([
        (END_GAME_COMMAND, BYE_MESSAGE),
        ('STRAIGHT_BET 10 15', SUCCESS_MESSAGE),
        ('STRAIGHT_BET 40 10', INVALID_BET_MESSAGE),
        ('INVALID_BET 10 15', INVALID_BET_TYPE_MESSAGE),
        ('STRAIGHT_BET 20 200', NOT_ENOUGH_CASH_MESSAGE)
    ])
    def test_user_typing_return_message(self, input, expected_message):
        self.assertEqual(expected_message, self.game.play(input))

    @patch('ruleta.roulette.randint', return_value=30)
    def test_play_round_win(self, mock_randint):
        self.player = Player(50)
        self.game.croupier.add_bet(StraightBet([30], 25))
        self.assertEqual(WON_MESSAGE + '875 chips', self.game.play(GO_COMMAND))

    @patch('ruleta.roulette.randint', return_value=31)
    def test_play_round_lost(self, mock_randint):
        self.player = Player(50)
        self.game.croupier.add_bet(StraightBet([30], 25))
        self.assertEqual(LOST_MESSAGE, self.game.play(GO_COMMAND))
    
    def test_next_turn(self):
        self.assertEqual(
            'STRAIGHT_BET, COLOR_BET, EVENODD_BET, LOWHIGH_BET, STREET_BET, '
            'SIXLINE_BET, DOUBLE_BET, ONEDOZEN_BET, TWODOZEN_BET, TRIO_BET, QUADRUPLE_BET\n'
            'GO,\n'
            'END_GAME',
            self.game.next_turn(),
        )

    def test_show_board(self):
        pass
