# # Set up of all possible values of cards
# COLORS = ['yellow', 'blue', 'red', 'green']
# NUMBERS = list(range(0, 10))

# class Deck():

#     def __init__(self):
#         self.stack = self.createStack()
#         self.discard = []
#     # setter/getter

#     # createStack (with or without discard)
#     def createStack(self):
#         pass

#     # takeFromTop
#     def takeFromTop(self):
#         pass

#     # shuffleAll
#     def shuffleAll(self):
#         pass
from .stack import Stack
from .player import Player


class Uno():
    def __init__(self):
        self.is_playing = True
        self.stack = Stack()
        self.player = Player(self.stack)
        self.stack.put_card_in_discard()

    def play(self, command):
        if command == 'END GAME':
            self.is_playing = False
            return 'Bye'
        elif command == '0':
            return self.player.cards_player.pop(self.stack.stack_cards)
        else:
            card = self.player.selected_card(command)
            is_valid_card = card.is_valid(self.stack.discard_cards)
            if is_valid_card is False:
                return "Your card is not valid"
            else:
                self.player.cards_player.remove(card)
                self.stack.put_card_in_discard(card)
