import unittest
from parameterized import parameterized
from .stack import Stack
from .card import Card
from .card import (
    NumberCard,
    ReverseCard,
    WildCard,
    SkipCard,
    DrawFourCard,
    DrawTwoCard,
)


class TestStack(unittest.TestCase):

    def _count_type_cards(self, card_type):
        stack = Stack()
        types = {
            'number': NumberCard,
            'skip': SkipCard,
            'reverse': ReverseCard,
            'draw_two_cards': DrawTwoCard,
            'draw_four_cards': DrawFourCard,
            'wild': WildCard
        }
        count = 0
        for card in stack.stack_cards:
            if type(card) == types[card_type]:
                count += 1
        return count

    def test_take_card(self):
        stack = Stack()
        self.assertIsInstance(stack.take_card(), Card)

    def test_len_cards(self):
        stack = Stack()
        len_previous_stack = len(stack.stack_cards)
        stack.take_card()
        self.assertEqual(len_previous_stack-1, len(stack.stack_cards))

    @parameterized.expand([
        ('number', 80),
        ('skip', 8),
        ('reverse', 8),
        ('draw_two_cards', 8),
        ('draw_four_cards', 4),
        ('wild', 4)
    ])
    def test_stack_number_cards_quantity(self, card_type, quantity):
        self.assertEqual(self._count_type_cards(card_type), quantity)

    def test_stack_empty(self):
        stack = Stack()
        for i in range(0, 30):
            stack.discard.append(stack.take_card())
        stack.stack_cards = []
        stack.is_stack_empty()
        self.assertEqual(29, len(stack.stack_cards))
