import unittest
from .roulette import Roulette
from .bet import BetCreator, StraightBet
from .player import Player
from .game_roullete import GameRoulette
from .board import get_color_from_number
from .board import get_dozen_from_number
from parameterized import parameterized
# Exceptions
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .exceptions.out_of_cash_exception import OutOfCashException


class TestRuleta(unittest.TestCase):

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

    # Test for the player
    def test_player_bets_100_but_have_50_should_fail(self):
        player = Player(50)
        with self.assertRaises(OutOfCashException):
            player.dicrement_money(100)

    def test_player_have_100_bets_50_will_have_50(self):
        player = Player(100)
        player.dicrement_money(50)
        self.assertEqual(50, player.money)

    # Tests for the bet creator
    def test_straight_bet(self):
        bet_factory = BetCreator()
        bet = bet_factory.create('STRAIGHT_BET', [17], 100, Player(500))
        self.assertIsInstance(bet, StraightBet)

    def test_invalid_type_bet(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.validate_bet_type('INVALID_BET')

    # Test for the bets
    def test_invalid_straight_bet(self):
        with self.assertRaises(InvalidBetException):
            StraightBet([40], 17, Player(500))

    def test_valid_straight_bet(self):
        straight_bet = StraightBet([36], 18, Player(500))
        self.assertEqual(36, straight_bet.bet_value)

    def test_player_win_straight_bet(self):
        straight_bet = StraightBet([36], 10, Player(500))
        straight_bet.win_bet(36)
        self.assertEqual(850, straight_bet.player.money)

    # Test for the game roullete
    def test_resolve_command_method(self):
        game = GameRoulette()
        result = game.resolve_command('STRAIGHT_BET 14 100')
        self.assertEqual(('STRAIGHT_BET', [14], 100), result)

    def test_user_type_END_and_next_turn_method_return_GAMEOVER(self):
        game = GameRoulette()
        game.play('END_GAME')
        self.assertEqual('Game over', game.next_turn())


if __name__ == '__main__':
    unittest.main()
