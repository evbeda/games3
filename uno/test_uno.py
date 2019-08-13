import unittest
from .card import NumberCard, ReverseCard, WildCard, SkipCard, DrawFourCard, DrawTwoCard
from .const import RED, YELLOW


class TestUno(unittest.TestCase):

    def test_same_to_skip_card_valid_color(self):
        top_card = SkipCard(RED)
        number_card = NumberCard(RED, '1')
        skip_card = SkipCard(RED)
        reverse_card = ReverseCard(RED)
        draw_two_card = DrawTwoCard(RED)
        wild_card = WildCard()
        draw_four_card = DrawFourCard()
        self.assertTrue(top_card.same_to(number_card))
        self.assertTrue(top_card.same_to(skip_card))
        self.assertTrue(top_card.same_to(reverse_card))
        self.assertTrue(top_card.same_to(draw_two_card))
        self.assertTrue(top_card.same_to(wild_card))
        self.assertTrue(top_card.same_to(draw_four_card))

    def test_same_to_skip_card_invalid_color(self):
        top_card = SkipCard(RED)
        number_card = NumberCard(YELLOW, '1')
        skip_card = SkipCard(YELLOW)
        reverse_card = ReverseCard(YELLOW)
        draw_two_card = DrawTwoCard(YELLOW)
        self.assertFalse(top_card.same_to(number_card))
        self.assertFalse(top_card.same_to(skip_card))
        self.assertFalse(top_card.same_to(reverse_card))
        self.assertFalse(top_card.same_to(draw_two_card))

    def test_same_to_reverse_card_valid_color(self):
        top_card = ReverseCard(RED)
        number_card = NumberCard(RED, '1')
        skip_card = SkipCard(RED)
        reverse_card = ReverseCard(RED)
        draw_two_card = DrawTwoCard(RED)
        wild_card = WildCard()
        draw_four_card = DrawFourCard()
        self.assertTrue(top_card.same_to(number_card))
        self.assertTrue(top_card.same_to(skip_card))
        self.assertTrue(top_card.same_to(reverse_card))
        self.assertTrue(top_card.same_to(draw_two_card))
        self.assertTrue(top_card.same_to(wild_card))
        self.assertTrue(top_card.same_to(draw_four_card))

    def test_same_to_reverse_card_invalid_color(self):
        top_card = ReverseCard(RED)
        number_card = NumberCard(YELLOW, '1')
        skip_card = SkipCard(YELLOW)
        reverse_card = ReverseCard(YELLOW)
        draw_two_card = DrawTwoCard(YELLOW)
        self.assertFalse(top_card.same_to(number_card))
        self.assertFalse(top_card.same_to(skip_card))
        self.assertFalse(top_card.same_to(reverse_card))
        self.assertFalse(top_card.same_to(draw_two_card))


if __name__ == '__main__':
    unittest.main()
