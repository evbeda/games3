
class Player():

    def __init__(self, cards_player):
        self.cards_player = cards_player
        self.loses_turn = False

    def selected_card(self, index_card):
        for index, card in enumerate(self.cards_player):
            if index == index_card - 1:
                return card
