from .card import DrawTwoCard, DrawFourCard


class Player():

    def __init__(self, cards):
        self.cards_player = cards
        self.already_take_a_card = False

    # def selected_card(self, index_card):
    #     return self.cards[int(index_card) - 1]

    # def auto_play(self, last_card):
    #     if isinstance(last_card, DrawTwoCard):
    #         draw_two_cards = [card for card in self.cards_player
    #                           if isinstance(card, DrawTwoCard)]
    #         if draw_two_cards != []:
    #             card = draw_two_cards[0]
    #             card = self.cards_player.pop(self.cards_player.index(card))
    #             return card
    #         else:
    #             return None
    #     for card in self.cards_player:
    #         if card.is_valid(last_card):
    #             card_selected = self.cards_player.pop(self.cards_player.index(card))
    #             return card_selected
    #     return None


class HumanPlayer(Player):
    def __init___(self, cards):
        super().__init__(cards)

    def select_card(self, card_index, stack):
        card = self.cards_player[card_index]
        if not card.is_valid(stack.get_last_discard_card):
            raise Exception()
        return card
