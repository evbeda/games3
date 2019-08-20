from .card import DrawTwoCard, DrawFourCard


class Player():

    def __init__(self, cards_player, name='Player',):
        self.name = name
        self.cards_player = cards_player
        self.loses_turn = False

    def selected_card(self, index_card):
        return self.cards_player[index_card]

    def add_cards_to_hand(self, cards):
        for card in cards:
            self.cards_player.append(card)

    def auto_play(self, last_card):
        if isinstance(last_card, DrawTwoCard):
            draw_two_cards = [card for card in self.cards_player
                              if isinstance(card, DrawTwoCard)]
            if draw_two_cards != []:
                card = draw_two_cards[0]
                card = self.cards_player.pop(self.cards_player.index(card))
                return card
            else:
                return None
        for card in self.cards_player:
            if card.is_valid(last_card):
                card_selected = self.cards_player.pop(self.cards_player.index(card))
                return card_selected
        return None
