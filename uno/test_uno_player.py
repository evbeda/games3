import unittest
from .player import HumanPlayer, ComputerPlayer
from .stack import Stack
from .card import (
    NumberCard,
    # WildCard,
    # DrawTwoCard,
)
from .const import GREEN, RED


class TestPlayerUno(unittest.TestCase):
    def setUp(self):
        self.player = HumanPlayer([])
        self.computer_player = ComputerPlayer([])
        self.stack = Stack()

    def test_human_select_valid_colored_card(self):
        valid_card = NumberCard(GREEN, 2)
        self.stack.discard_cards = [valid_card]
        self.player.cards_player = [valid_card]
        card = self.player.select_card(0, self.stack)
        self.assertEqual(card, valid_card)

    def test_human_select_invalid_colored_card(self):
        top_card = NumberCard(RED, 5)
        invalid_card = NumberCard(GREEN, 2)
        self.stack.discard_cards = [top_card]
        self.player.cards_player = [invalid_card]
        with self.assertRaises(Exception):
            self.player.select_card(0, self.stack)
        with self.assertRaises(Exception):
            self.player.select_card(1, self.stack)

    def test_computer_select_valid_colored_card(self):
        valid_card = NumberCard(GREEN, 2)
        self.stack.discard_cards = [valid_card]
        self.computer_player.cards_player = [valid_card]
        card = self.computer_player.select_card(0, self.stack)
        self.assertEqual(card, valid_card)

    def test_computer_select_with_no_valid_cards(self):
        top_card = NumberCard(RED, 5)
        invalid_card = NumberCard(GREEN, 2)
        self.stack.discard_cards = [top_card]
        self.computer_player.cards_player = [invalid_card]
        self.assertEqual(self.computer_player.select_card(0, self.stack), None)

