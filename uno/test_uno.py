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

    def test_number_card(self):

        top_card = NumberCard(RED, '0')

        # TEST NUMBER - NUMBER
        selected_card_same_color = NumberCard(RED, '2')
        selected_card_same_number = NumberCard(YELLOW, '0')
        selected_card_no_equal = NumberCard(YELLOW, '3')

        self.assertTrue(top_card.same_to(selected_card_same_color))
        self.assertTrue(top_card.same_to(selected_card_same_number))
        self.assertFalse(top_card.same_to(selected_card_no_equal))

        # TEST NUMBER - SKIP
        selected_card_same_color = SkipCard(RED)
        selected_card_no_equal = SkipCard(YELLOW)

        self.assertTrue(top_card.same_to(selected_card_same_color))
        self.assertFalse(top_card.same_to(selected_card_no_equal))

        # TEST NUMBER - REVERSE
        selected_card_same_color = ReverseCard(RED)
        selected_card_no_equal = ReverseCard(YELLOW)
        
        self.assertTrue(top_card.same_to(selected_card_same_color))
        self.assertFalse(top_card.same_to(selected_card_no_equal))

        # TEST NUMBER - DRAWFOUR
        selected_card = DrawFourCard()
                
        self.assertTrue(top_card.same_to(selected_card))

        # TEST NUMBER - DRAWTWO
        selected_card_same_color = DrawTwoCard(RED)
        selected_card_no_equal = DrawTwoCard(YELLOW)
                
        self.assertTrue(top_card.same_to(selected_card_same_color))
        self.assertFalse(top_card.same_to(selected_card_no_equal))

        # TEST NUMBER - WILDCARD
        selected_card = WildCard()
                
        self.assertTrue(top_card.same_to(selected_card))




if __name__ == '__main__':
    unittest.main()
