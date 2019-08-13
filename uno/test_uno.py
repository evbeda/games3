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

    def test_number_same_to_number_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_color = NumberCard(RED, '2')
        self.assertTrue(top_card.same_to(selected_card_same_color))
    
    def test_number_same_to_number_same_number(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_number = NumberCard(YELLOW, '0')
        self.assertTrue(top_card.same_to(selected_card_same_number))
    
    def test_number_same_to_number_no_equal(self):
        top_card = NumberCard(RED, '0')
        selected_card_no_equal = NumberCard(YELLOW, '3')
        self.assertFalse(top_card.same_to(selected_card_no_equal))

    def test_number_same_to_skip_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_color = SkipCard(RED)
        self.assertTrue(top_card.same_to(selected_card_same_color))

    def test_number_same_to_skip_no_equal(self):
        top_card = NumberCard(RED, '0')
        selected_card_no_equal = SkipCard(YELLOW)
        self.assertFalse(top_card.same_to(selected_card_no_equal))

    def test_number_same_to_reverse_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_color = ReverseCard(RED)
        self.assertTrue(top_card.same_to(selected_card_same_color))
    
    def test_number_same_to_reverse_no_equal(self):
        top_card = NumberCard(RED, '0')
        selected_card_no_equal = ReverseCard(YELLOW)
        self.assertFalse(top_card.same_to(selected_card_no_equal))

    def test_number_same_to_draw_four(self):
        top_card = NumberCard(RED, '0')
        selected_card = DrawFourCard()    
        self.assertTrue(top_card.same_to(selected_card))

    def test_number_same_to_draw_two_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_color = DrawTwoCard(RED)
        self.assertTrue(top_card.same_to(selected_card_same_color))

    def test_number_same_to_draw_two_no_equal(self):
        top_card = NumberCard(RED, '0')
        selected_card_no_equal = DrawTwoCard(YELLOW)
        self.assertFalse(top_card.same_to(selected_card_no_equal))

    def test_number_same_to_wild_card(self):
        top_card = NumberCard(RED, '0')
        selected_card = WildCard()
        self.assertTrue(top_card.same_to(selected_card))

    def test_same_type_skip_card_different_color(self):
        top_card = SkipCard(RED)
        selected_card = SkipCard(YELLOW)
        self.assertTrue(top_card.same_type_validator(top_card, selected_card))

    def test_same_type_reverse_card_different_color(self):
        top_card = ReverseCard(RED)
        selected_card = ReverseCard(YELLOW)
        self.assertTrue(top_card.same_type_validator(top_card, selected_card))
        
    def test_same_type_draw_two_different_color(self):
        top_card = DrawTwoCard(RED)
        selected_card = DrawTwoCard(YELLOW)
        self.assertTrue(top_card.same_type_validator(top_card, selected_card))

    def test_draw_two_card_to_draw_two_card(self):
        top_card = DrawTwoCard(RED)
        selected_card = DrawTwoCard(YELLOW)
        self.assertEqual(selected_card.action(top_card), 4)

    def test_draw_two_cards_to_number_card_with_same_color(self):
        top_card = NumberCard(RED, 2))
        selected_card = DrawTwoCard(RED)
        self.assertEqual(selected_card.action(top_card), 2)


if __name__ == '__main__':
    unittest.main()
