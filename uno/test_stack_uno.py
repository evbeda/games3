# Modules
import unittest
from unittest.mock import patch
from parameterized import parameterized
# Model
from .stack import Stack
from .card import (
    NumberCard,
    ReverseCard,
    WildCard,
    SkipCard,
    DrawFourCard,
    DrawTwoCard,
)
# Model
from .const import YELLOW, RED


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.STACK_EXAMPLE = [
                            NumberCard(RED, 5),
                            NumberCard(YELLOW, 4)
                        ]

        self.DYING_STACK_EXAMPLE = [NumberCard(YELLOW, 4)]

    def _count_type_cards(self, card_type):
        types = {
            'number': NumberCard,
            'skip': SkipCard,
            'reverse': ReverseCard,
            'draw_two_cards': DrawTwoCard,
            'draw_four_cards': DrawFourCard,
            'wild': WildCard
        }
        count = 0
        for card in self.stack.stack_cards:
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
        for i in range(0, 30):
            self.stack.discard_cards.append(self.stack.stack_cards.pop())
        self.stack.stack_cards = []
        discard_cards = self.stack.discard_cards
        self.stack.recreate_stack()
        for i in self.stack.stack_cards:
            self.assertIn(i, discard_cards)

    def test_cards_player(self):
        cards_player = self.stack.generate_cards_player()
        self.assertEqual(7, len(cards_player))

    def test_get_last_discard_card(self):
        self.stack.discard_cards = self.STACK_EXAMPLE
        card = self.stack.get_last_discard_card
        self.assertEqual((YELLOW, 4), (card.color, card.number))

    def test_draw_card_from_stack_should_return_last_card_from_stack(self):
        self.stack.stack_cards = self.STACK_EXAMPLE
        card = self.stack.draw_card_from_stack()
        self.assertEqual((YELLOW, 4), (card.color, card.number))

    def test_draw_card_from_stack_should_reduce_qty_of_stack(self):
        self.stack.stack_cards = self.STACK_EXAMPLE
        prevLen = len(self.stack.stack_cards)
        self.stack.draw_card_from_stack()
        self.assertGreater(prevLen, len(self.stack.stack_cards))

    @patch('uno.stack.Stack.recreate_stack')
    def test_draw_last_card_from_stack_should_recreate_stack(
            self, recreate_stack_mock):
        self.stack.stack_cards = self.DYING_STACK_EXAMPLE
        self.stack.draw_card_from_stack()
        recreate_stack_mock.assert_called()

    def test_draw_last_card_from_stack(self):
        self.stack.stack_cards = self.DYING_STACK_EXAMPLE
        self.stack.discard_cards = self.STACK_EXAMPLE
        self.stack.draw_card_from_stack()
        self.assertGreater(len(self.stack.stack_cards), 0)
