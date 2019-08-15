import unittest
from .card import NumberCard, ReverseCard, WildCard, SkipCard, DrawFourCard, DrawTwoCard
from .stack import Stack
from .const import RED, YELLOW, GREEN, BLUE
from parameterized import parameterized


class TestUno(unittest.TestCase):

    # Falta dividir los test cases
    @parameterized.expand([
        (SkipCard(RED), NumberCard(RED, '1')),
        (SkipCard(RED), SkipCard(RED)),
        (SkipCard(RED), ReverseCard(RED)),
        (SkipCard(RED), DrawTwoCard(RED)),
        (SkipCard(RED), WildCard()),
        (SkipCard(RED), DrawFourCard())
    ])
    def test_same_to_skip_card_valid_color(self, top_card, selected_card):
        self.assertTrue(top_card.same_to(selected_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(YELLOW, '1')),
        (SkipCard(RED), SkipCard(YELLOW)),
        (SkipCard(RED), ReverseCard(YELLOW)),
        (SkipCard(RED), DrawTwoCard(YELLOW)),
    ])
    def test_same_to_skip_card_invalid_color(self, top_card, selected_card):
        self.assertFalse(top_card.same_to(selected_card))

    @parameterized.expand([
        (ReverseCard(RED), NumberCard(RED, '1')),
        (ReverseCard(RED), SkipCard(RED)),
        (ReverseCard(RED), ReverseCard(RED)),
        (ReverseCard(RED), DrawTwoCard(RED)),
        (ReverseCard(RED), WildCard()),
        (ReverseCard(RED), DrawFourCard())
    ])
    def test_same_to_reverse_card_valid_color(self, top_card, selected_card):
        self.assertTrue(top_card.same_to(selected_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(YELLOW, '1')),
        (SkipCard(RED), SkipCard(YELLOW)),
        (SkipCard(RED), ReverseCard(YELLOW)),
        (SkipCard(RED), DrawTwoCard(YELLOW)),
    ])
    def test_same_to_reverse_card_invalid_color(self, top_card, selected_card):
        self.assertFalse(top_card.same_to(selected_card))

# Refactorizar un solo test, que pruebe con los 9 numeros y el mismo color.
    def test_number_same_to_number_same_color(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_color = NumberCard(RED, '2')
        self.assertTrue(top_card.same_to(selected_card_same_color))

# Refactorizar un solo test que pruebe los 4 0 de distinto color.
    def test_number_same_to_number_same_number(self):
        top_card = NumberCard(RED, '0')
        selected_card_same_number = NumberCard(YELLOW, '0')
        self.assertTrue(top_card.same_to(selected_card_same_number))

# Refactorizar un solo test, que pruebe con los numeros erroneos y distinto color.
    def test_number_same_to_number_no_equal(self):
        top_card = NumberCard(RED, '0')
        selected_card_no_equal = NumberCard(YELLOW, '3')
        self.assertFalse(top_card.same_to(selected_card_no_equal))

# Refactorizar un solo test, que pruebe un numero con el color de las especiales (skip, reverse y +2)
    @parameterized.expand([
        (NumberCard(RED, '1'), SkipCard(RED)),
        (NumberCard(RED, '1'), ReverseCard(RED)),
        (NumberCard(RED, '1'), DrawTwoCard(RED)),
        (NumberCard(RED, '1'), WildCard()),
        (NumberCard(RED, '1'), DrawFourCard())
    ])
    def test_number_same_to_skip_same_color(self, top_card, selected_card):
        self.assertTrue(top_card.same_to(selected_card))

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

    @parameterized.expand([
        (SkipCard(RED), SkipCard(YELLOW)),
        (ReverseCard(RED), ReverseCard(RED)),
        (DrawTwoCard(RED), DrawTwoCard(YELLOW))
    ])
    def test_same_type_skip_card_different_color(self, top_card, selected_card):
        self.assertTrue(top_card.same_type_validator(top_card, selected_card))

    def test_draw_two_card_to_draw_two_card(self):
        top_card = DrawTwoCard(RED)
        selected_card = DrawTwoCard(YELLOW)
        self.assertEqual(selected_card.action(top_card), 4)

    def test_draw_two_cards_to_number_card_with_same_color(self):
        top_card = NumberCard(RED, 2)
        selected_card = DrawTwoCard(RED)
        self.assertEqual(selected_card.action(top_card), 2)

    @parameterized.expand([
            (DrawFourCard, DrawFourCard),
            (DrawFourCard, DrawTwoCard(YELLOW)),
            (DrawFourCard, ReverseCard(RED)),
            (DrawFourCard, SkipCard(GREEN)),
            (DrawFourCard, NumberCard(BLUE, '5'))
        ])
    def test_draw_four_card_to_any_card(self, top_card, selected_card):
        self.assertTrue(top_card.evaluate_next_card(top_card, selected_card))

    @parameterized.expand([
        ('number', 80),
        ('skip', 8),
        ('reverse', 8),
        ('draw_two_cards', 8),
        ('draw_four_cards', 4),
        ('wild', 4)
    ])
    def test_stack_number_cards_quantity(self, card_type, quantity):
        stack = Stack()
        self.assertEqual(stack.count_type_cards(card_type), quantity)


if __name__ == '__main__':
    unittest.main()
