import unittest
from .roulette import Roulette
from .bet import BetCreator, StraightBet
from .player import Player
from .game_roullete import GameRoulette
# Exceptions
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .exceptions.out_of_cash_exception import OutOfCashException


class TestRuleta(unittest.TestCase):

    # Test for the roullete
    def test_numbers(self):
        ruleta = Roulette()
        number = ruleta.generate_number()
        self.assertTrue(number >= 0 and number <= 36)

    def test_history(self):
        ruleta = Roulette()
        number = ruleta.generate_number()
        last_numbers = ruleta.get_last_numbers()
        self.assertTrue(last_numbers[-1] == number)

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
