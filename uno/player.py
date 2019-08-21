from random import choice
from .card import DrawTwoCard


class Player():

    def __init__(self, cards_player):
        self.cards_player = cards_player
        self.loses_turn = False

    def play(self, parsed_card, last_card):
        pass

    def add_cards_to_hand(self, cards):
        for card in cards:
            self.cards_player.append(card)


class HumanPlayer(Player):
    def __init__(self, cards_player):
        super.__init__(cards_player)

    def play(self, parsed_card, last_card):
        # If is valid
        if True:
            return self.cards_player[parsed_card]
        else:
            return None


class ComputerPlayer(Player):
    def __init__(self, cards_player):
        super.__init__(cards_player)

    def play(self, parsed_card, last_card):
        if isinstance(last_card, DrawTwoCard):
            draw_two_cards = [card for card in self.cards_player
                              if isinstance(card, DrawTwoCard)]
            if draw_two_cards != []:
                card = draw_two_cards[0]
                card = self.cards_player.pop(self.cards_player.index(card))
                return card
            else:
                return None
        else:
            possible_cards = [card for card in self.cards_player
                              if card.is_valid(last_card)]
            if possible_cards:
                return None
            else:
                return choice(possible_cards)
