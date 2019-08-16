import unittest
from parameterized import parameterized
from .roulette import Roulette
from .bet import BetCreator, StraightBet, ColorBet, EvenOddBet
from .player import Player
from .game_roullete import GameRoulette
from .board import get_color_from_number
from .board import get_dozen_from_number
from .croupier import Croupier

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
]


class TestRuleta(unittest.TestCase):

    def setUp(self):
        self.player = Player(100)
        self.croupier = Croupier(self.player)

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
    def test_straight_bet(self):
        bet = BetCreator.create('STRAIGHT_BET', [17], 100)
        self.assertIsInstance(bet, StraightBet)

    def test_invalid_type_bet(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.validate_bet_type('INVALID_BET')

    # Test for the bets
    @parameterized.expand([
        (StraightBet, [40], 17),
        (ColorBet, ['Reds'], 300),
        (EvenOddBet, ['ODDs'], 30)
    ])
    def test_invalid_bets(self, bet, bet_value, ammount):
        with self.assertRaises(InvalidBetException):
            bet(bet_value, ammount)

    @parameterized.expand(bet_scenario)
    def test_valid_bets(self,
                        bet,
                        bet_value,
                        ammount,
                        award,
                        chosen_number,
                        expect_winner):
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
            award
        )

    # Test for the game roullete
    def test_resolve_command_method(self):
        game = GameRoulette()
        result = game.resolve_command('STRAIGHT_BET 14 100')
        self.assertEqual(('STRAIGHT_BET', [14], 100), result)

    def test_user_type_END_and_next_turn_method_return_GAMEOVER(self):
        game = GameRoulette()
        game.play('END_GAME')
        self.assertEqual('Game over', game.next_turn())

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
        self.assertEqual(1, len(self.croupier.bets))


if __name__ == '__main__':
    unittest.main()
