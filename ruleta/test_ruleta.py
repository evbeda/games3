import unittest
from unittest.mock import patch
from parameterized import parameterized
from .roulette import Roulette
from .bet import (
    BetCreator,
    StraightBet,
    ColorBet,
    EvenOddBet,
    LowHighBet,
    StreetBet,
    SixLineBet,
    DoubleBet,
)
from .player import Player
from .game_roullete import GameRoulette
from .board import get_color_from_number
from .board import get_dozen_from_number
from .croupier import Croupier

# Messages
from . import (
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
# Exceptions
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .exceptions.out_of_cash_exception import OutOfCashException

bet_scenario = [
    # tipo de apuesta, tipo_input, amount, prize, number chosen, won/lose
    (StraightBet, [36], 25, 875, 36, True),
    (ColorBet, ['Red'], 300, 600, 36, True),
    (EvenOddBet, ['ODD'], 30, 0, 36, False),
    (StraightBet, [36], 25, 0, 35, False),
    (ColorBet, ['Red'], 300, 0, 35, False),
    (EvenOddBet, ['ODD'], 30, 60, 35, True),
    (StreetBet, [13, 14, 15], 10, 110, 14, True),
    (StreetBet, [13, 14, 15], 10, 0, 10, False),
    (SixLineBet, [1, 4], 30, 150, 6, True),
    (SixLineBet, [1, 4], 30, 0, 8, False),
    (DoubleBet, [1, 2], 50, 850, 2, True),
    (DoubleBet, [1, 2], 50, 0, 5, False),
]

RED_CORRECT_VALUES = \
    [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

BLACK_CORRECT_VALUES = \
    [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


class TestRuleta(unittest.TestCase):

    def setUp(self):
        self.player = Player(100)
        self.croupier = Croupier(self.player)
        self.game = GameRoulette()

    # Test for the roullete
    def test_numbers(self):
        roulette = Roulette()
        number = roulette.generate_number()
        self.assertTrue(number in list(range(0, 37)))

    def test_history(self):
        roulette = Roulette()
        number = roulette.generate_number()
        last_numbers = roulette.get_last_numbers()
        self.assertTrue(last_numbers[-1] == number)

    # Test for the Board
    @parameterized.expand([
        (36,), (1,), (3,), (5,), (7,), (9,), (12,), (14,), (16,), (18,),
        (19,), (21,), (23,), (25,), (27,), (30,), (32,), (34,), (36,),
    ])
    def test_get_color_red_from_last_number(self, number):
        self.assertEqual('red', get_color_from_number(number))

    @parameterized.expand([
        (2,), (4,), (6,), (8,), (10,), (11,), (13,), (15,), (17,), (20,),
        (22,), (24,), (26,), (28,), (29,), (31,), (33,), (35,),
    ])
    def test_get_color_black_from_last_number(self, number):
        self.assertEqual('black', get_color_from_number(number))

    def test_get_color_green_from_last_number(self):
        self.assertEqual('green', get_color_from_number(0))

    @parameterized.expand([
        (1, 1), (3, 1), (5, 1), (7, 1), (9, 1), (12, 1),
        (14, 2), (16, 2), (18, 2), (19, 2), (21, 2), (24, 2),
        (25, 3), (27, 3), (30, 3), (32, 3), (34, 3), (36, 3),
    ])
    def test_get_dozen_from_last_number(self, number, dozen):
        self.assertEqual(dozen, get_dozen_from_number(number))

    # Tests for the bet creator
    @parameterized.expand([
        ('STRAIGHT_BET', [15], 17, StraightBet),
        ('COLOR_BET', ['Red'], 300, ColorBet),
        ('EVENODD_BET', ['ODD'], 30, EvenOddBet),
        ('LOWHIGH_BET', ['Low'], 11, LowHighBet),
        ('STREET_BET', [16, 17, 18], 100, StreetBet),
        ('SIXLINE_BET', [16, 19], 10, SixLineBet),
        ('DOUBLE_BET', [23, 24], 30, DoubleBet),
    ])
    def test_bet_creator(
            self, bet_type, bet_values, amount, expected_instance):
        bet = BetCreator.create(bet_type, bet_values, amount)
        self.assertIsInstance(bet, expected_instance)

    def test_invalid_type_bet(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.validate_bet_type('INVALID_BET')

    # Test for the bets
    @parameterized.expand([
        (StraightBet, [40], 17),
        (ColorBet, ['Reds'], 300),
        (EvenOddBet, ['ODDs'], 30),
        (LowHighBet, ['Lower'], 11),
        (StreetBet, [1, 2, 4], 100),
        (SixLineBet, [12, 13], 10),
        (DoubleBet, [0, 36], 100),
        (DoubleBet, [0, 0], 50)
    ])
    def test_invalid_bets(self, bet, bet_value, ammount):
        with self.assertRaises(InvalidBetException):
            bet(bet_value, ammount)

    # Test for the bets
    @parameterized.expand([
        (StraightBet, [30], [30]),
        (ColorBet, ['Red'], RED_CORRECT_VALUES),
        (ColorBet, ['black'], BLACK_CORRECT_VALUES),
        (EvenOddBet, ['ODD'], [x for x in range(1, 37) if x % 2 == 1]),
        (EvenOddBet, ['EvEN'], [x for x in range(1, 37) if x % 2 == 0]),
        (LowHighBet, ['Low'], [x for x in range(1, 19)]),
        (LowHighBet, ['high'], [x for x in range(19, 37)]),
        (StreetBet, [1, 2, 3], [1, 2, 3]),
        (SixLineBet, [25, 28], [25, 26, 27, 28, 29, 30]),
        (DoubleBet, [2, 5], [2, 5]),
        (DoubleBet, [33, 36], [33, 36]),
        (DoubleBet, [1, 2], [1, 2]),
        (DoubleBet, [0, 3], [0, 3]),
        (DoubleBet, [4, 7], [4, 7])
    ])
    def test_valid_bets(self, bet, bet_value, expected_target_numbers):
        bet = bet(bet_value, 10)
        self.assertEqual(bet.target_numbers, expected_target_numbers)

    @parameterized.expand(bet_scenario)
    def test_is_winner(
            self, bet, bet_value, ammount, award, chosen_number, expect_winner
            ):
        bet_type = bet(bet_value, ammount)
        self.assertEqual(bet_type.is_winner(chosen_number), expect_winner)

    @parameterized.expand(bet_scenario)
    def test_win_bet(
        self,
        bet,
        bet_value,
        ammount,
        award,
        chosen_number,
        expected_winner,
    ):
        bet_type = bet(bet_value, ammount)
        self.assertEqual(
            bet_type.calculate_award(chosen_number),
            award,
        )

    # Test for the game roullete
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

    # Test for the croupier
    def test_player_bets_100_but_have_50_should_fail(self):
        self.croupier = Croupier(Player(50))
        with self.assertRaises(OutOfCashException):
            self.croupier.discount_money_from_player(100)

    def test_player_have_100_bets_50_will_have_50(self):

        self.croupier.discount_money_from_player(50)
        self.assertEqual(50, self.player.money)

    def test_croupier_add_a_bet(self):
        self.croupier.add_bet(StraightBet([13], 10))
        self.assertEqual(1, len(self.croupier.round.bets))

    @patch('ruleta.roulette.randint', return_value=30)
    def test_croupier_add_reward_to_player(self, mock_randint):
        self.player = Player(50)
        self.croupier = Croupier(self.player)
        self.croupier.add_bet(StraightBet([30], 25))
        self.croupier.add_bet(EvenOddBet(['even'], 10))
        self.croupier.add_bet(LowHighBet(['low'], 5))
        self.croupier.play()
        self.assertEqual(self.player.money, 905)


if __name__ == '__main__':
    unittest.main()
