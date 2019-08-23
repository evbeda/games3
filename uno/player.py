from random import choice
from .exceptions import ComputerCantPlayException


class Player():

    def __init__(self, cards):
        self.cards_player = cards
        self.has_drawn_a_card = False

    def raise_exception(self):
        raise Exception()

    def condition(self, top_card, card_index=None):
        pass

    def calculate_index(self, top_card):
        pass

    def select_card(self, top_card, card_index=None):
        if not self.condition(top_card, card_index):
            self.raise_exception()
        if card_index is not None:
            return self.cards_player.pop(card_index)
        else:
            return self.cards_player.pop(self.calculate_index(top_card))


class HumanPlayer(Player):
    def __init___(self, cards):
        super().__init__(cards)

    def __str__(self):
        return 'Player'

    def raise_exception(self):
        raise Exception()

    def condition(self, top_card, card_index=None):
        return self.cards_player[card_index].is_valid(top_card)


class ComputerPlayer(Player):
    def __init__(self, cards):
        super().__init__(cards)

    def __str__(self):
        return 'Computer'

    def raise_exception(self):
        raise ComputerCantPlayException()

    def condition(self, top_card, card_index=None):
        return [
            card for card in self.cards_player
            if card.is_valid(top_card)
        ]

    def calculate_index(self, top_card):
        possible_cards = [
            card for card in self.cards_player
            if card.is_valid(top_card)
        ]
        return self.cards_player.index(choice(possible_cards))
