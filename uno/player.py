

class Player():

    def __init__(self, stack):
        self.cards_player = stack.generated_cards_player()  

    def selected_card(self, index_card):
        for index, value in enumerate(self.cards_player):
            if index == index_card:
                return value
