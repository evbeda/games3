import unittest
from uno.card import NumberCard, ReverseCard, WildCard
from uno.const import RED


class TestUno(unittest.TestCase):

    def test_same_to_color(self):

        # Create cards (top and playable card)
        top_card = NumberCard(RED, '0')
        selected_card = ReverseCard(RED)
        self.assertTrue(top_card.same_to(selected_card))

    def test_wild_card_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card = WildCard()
        self.assertTrue(top_card.same_to(selected_card))


if __name__ == '__main__':
    unittest.main()
