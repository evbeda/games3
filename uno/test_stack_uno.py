import unittest
from parameterized import parameterized
from .stack import Stack
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
            stack.discard_cards.append(stack.stack_cards.pop())
        stack.stack_cards = []
        discard_cards = stack.discard_cards
        stack.recreate_stack()
        for i in stack.stack_cards:
            self.assertIn(i, discard_cards)

    def test_cards_player(self):
        stack = Stack()
        cards_player = stack.generate_cards_player()
        self.assertEqual(7, len(cards_player))
