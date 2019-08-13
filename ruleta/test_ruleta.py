import unittest
from roulette import Roulette
from bet import BetCreator, StraightBet


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
        bet = bet_factory.create(1, 17, 100)
        self.assertIsInstance(bet, StraightBet)

    def test_validate_straight_bet(self):
        for i in range(37):
            test = True
            if StraightBet.validate_straight(i):
                continue
            else:
                test = False
                break
        self.assertTrue(test)
        # self.assertFalse(StraightBet.validate_straight(40))


if __name__ == '__main__':
    unittest.main()
