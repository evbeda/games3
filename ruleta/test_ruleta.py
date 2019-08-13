import unittest
from .roulette import Roulette
from .bet import BetCreator, StraightBet
from .player import Player
# Exceptions
from .exceptions.invalid_bet_exception import InvalidBetException


class TestRuleta(unittest.TestCase):
    def test_numbers(self):
        ruleta = Roulette()
        number = ruleta.generate_number()
        self.assertTrue(number >= 0 and number <= 36)

    def test_history(self):
        ruleta = Roulette()
        number = ruleta.generate_number()
        last_numbers = ruleta.get_last_numbers()
        self.assertTrue(last_numbers[-1] == number)

    def test_straight_bet(self):
        # a bet is created
        bet_factory = BetCreator()
        bet = bet_factory.create(1, 17, 100, Player(500))
        self.assertIsInstance(bet, StraightBet)

    def test_invalid_straight_bet(self):
        with self.assertRaises(InvalidBetException):
            StraightBet(40, 17, Player(500))

    def test_valid_straight_bet(self):
        straight_bet = StraightBet(36, 18, Player(500))
        self.assertEqual(36, straight_bet.bet_value)

    def test_player_win_straight_bet(self):
        straight_bet = StraightBet(36, 10, Player(500))
        straight_bet.win_bet(36)
        self.assertEqual(850, straight_bet.player.money)

if __name__ == '__main__':
    unittest.main()
