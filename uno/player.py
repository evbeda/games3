from random import choice
from .exceptions import ComputerCantPlayException


class Player():

    def __init__(self, cards):
        self.cards_player = cards
        self.has_drawn_a_card = False


class HumanPlayer(Player):
    def __init___(self, cards):
        super().__init__(cards)

    def __str__(self):
        return 'Player'

    def select_card(self, card_index, stack):
        card = self.cards_player[card_index]
        if not card.is_valid(stack.top_card):
            raise Exception()
        return self.cards_player.pop(card_index)


class ComputerPlayer(Player):
    def __init__(self, cards):
        super().__init__(cards)

    def __str__(self):
        return 'Computer'

    def select_card(self, stack):
        possible_cards = [
            card for card in self.cards_player
            if card.is_valid(stack.top_card)
        ]
        if possible_cards:
            return self.cards_player.pop(
                self.cards_player.index(choice(possible_cards)))
        else:
            raise ComputerCantPlayException
