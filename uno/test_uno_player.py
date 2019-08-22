import unittest
from .player import HumanPlayer
from .stack import Stack
from .card import (
    NumberCard,
    # WildCard,
    # DrawTwoCard,
)
from .const import GREEN, RED, INVALID_CARD_MESSAGE


class TestPlayerUno(unittest.TestCase):
    def setUp(self):
        self.player = HumanPlayer([])
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


    # def test_auto_play(self):
    #     uno = Uno()
    #     wildcard = WildCard()
    #     uno.stack.discard_cards.append(NumberCard(GREEN, 4))
    #     uno.computer_player.cards_player.pop(0)
    #     uno.computer_player.cards_player.append(wildcard)
    #     card = uno.computer_player.auto_play(uno.stack.discard_cards[-1])
    #     self.assertTrue(card.is_valid(uno.stack.discard_cards[-1]))

    # def test_auto_play_after_draw_to(self):
    #     uno = Uno()
    #     draw_two = DrawTwoCard(GREEN)
    #     uno.computer_player.cards_player.append(draw_two)
    #     card = uno.computer_player.auto_play(draw_two)
    #     self.assertTrue(isinstance(card, DrawTwoCard))

    # def test_auto_play_after_draw_to_if_not_in_hand(self):
    #     """If the player don't have a draw to card, he can't play a card"""
    #     uno = Uno()
    #     draw_two = DrawTwoCard(GREEN)
    #     uno.computer_player.cards_player = [NumberCard(GREEN, 3)]
    #     card = uno.computer_player.auto_play(draw_two)
    #     self.assertTrue(card is None)

    # def test_auto_play_if_has_not_valid_card(self):
    #     """If the player don't have a valid card, he can't play a card"""
    #     uno = Uno()
    #     uno.computer_player.cards_player = [NumberCard(GREEN, 3)]
    #     card = uno.computer_player.auto_play(NumberCard(RED, 5))
    #     self.assertTrue(card is None)

    # def test_selected_card(self):
    #     card1 = NumberCard(GREEN, 3)
    #     card2 = NumberCard(RED, 4)
    #     card3 = NumberCard(BLUE, 5)
    #     cards = [card1, card2, card3]
    #     player = Player(cards)
    #     self.assertTrue(player.selected_card(2) == card3)
