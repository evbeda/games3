# Modules
from unittest import TestCase
from parameterized import parameterized

# Model classes
from ..bet import (
    BetCreator,
    StraightBet,
    ColorBet,
    EvenOddBet,
    LowHighBet,
    StreetBet,
    SixLineBet,
    DoubleBet,
)

# Exceptions
from ..exceptions.invalid_bet_exception import InvalidBetException
from ..exceptions.invalid_bet_type_exception import InvalidBetTypeException

# Const
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


class TestBetsRoulette(TestCase):
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


class TestBetCreator(TestCase):
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
