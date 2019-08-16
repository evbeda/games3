
class Player():

    def __init__(self, stack):
        self.cards_player = stack.generate_cards_player()

    def selected_card(self, index_card):
        for index, card in enumerate(self.cards_player):
            if index == index_card - 1:
                return card
