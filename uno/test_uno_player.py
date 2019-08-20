import unittest
from .player import Player
from .uno import Uno
from .card import (
    NumberCard,
    WildCard,
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
