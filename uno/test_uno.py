import unittest
from uno.card import NumberCard, ReverseCard


class TestUno(unittest.TestCase):

    def test_same_to_color(self):

        # Create cards (top and playable card)
        card1 = NumberCard('red', '0')
        card2 = ReverseCard('red')

        self.assertTrue(card1.same_to(card2))


if __name__ == '__main__':
    unittest.main()
