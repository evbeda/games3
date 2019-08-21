import unittest
from .player import Player
from .uno import Uno
from .card import (
    NumberCard,
    WildCard,
    DrawTwoCard,
)
from .const import GREEN, RED, BLUE


class TestPlayerUno(unittest.TestCase):

    def test_add_cards_to_hand(self):
        player = Player([])
        card = NumberCard(GREEN, 2)
        player.add_cards_to_hand([card])
        self.assertTrue(card in player.cards_player)

    def test_add_multiple_cards_to_hand(self):
        player = Player([])
        card1 = NumberCard(GREEN, 3)
        card2 = NumberCard(RED, 4)
        card3 = NumberCard(BLUE, 5)
        cards = [card1, card2, card3]
        player.add_cards_to_hand(cards)
        self.assertTrue(all(card in player.cards_player for card in cards))

    def test_auto_play(self):
        uno = Uno()
        wildcard = WildCard()
        uno.stack.discard_cards.append(NumberCard(GREEN, 4))
        uno.computer_player.cards_player.pop(0)
        uno.computer_player.cards_player.append(wildcard)
        card = uno.computer_player.auto_play(uno.stack.discard_cards[-1])
        self.assertTrue(card.is_valid(uno.stack.discard_cards[-1]))

    def test_auto_play_after_draw_to(self):
        uno = Uno()
        draw_two = DrawTwoCard(GREEN)
        uno.computer_player.cards_player.append(draw_two)
        card = uno.computer_player.auto_play(draw_two)
        self.assertTrue(isinstance(card, DrawTwoCard))

    def test_auto_play_after_draw_to_if_not_in_hand(self):
        """If the player don't have a draw to card, he can't play a card"""
        uno = Uno()
        draw_two = DrawTwoCard(GREEN)
        uno.computer_player.cards_player = [NumberCard(GREEN, 3)]
        card = uno.computer_player.auto_play(draw_two)
        self.assertTrue(card is None)

    def test_auto_play_if_has_not_valid_card(self):
        """If the player don't have a valid card, he can't play a card"""
        uno = Uno()
        uno.computer_player.cards_player = [NumberCard(GREEN, 3)]
        card = uno.computer_player.auto_play(NumberCard(RED, 5))
        self.assertTrue(card is None)

    # def test_selected_card(self):
    #     card1 = NumberCard(GREEN, 3)
    #     card2 = NumberCard(RED, 4)
    #     card3 = NumberCard(BLUE, 5)
    #     cards = [card1, card2, card3]
    #     player = Player(cards)
    #     self.assertTrue(player.selected_card(2) == card3)
