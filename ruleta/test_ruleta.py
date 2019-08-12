import unittest
from roulette import Roulette
from bet import Bet


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
        bet = Bet(1, 17, 100)

if __name__ == '__main__':
    unittest.main()
