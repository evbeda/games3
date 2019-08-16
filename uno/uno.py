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
            return self.player.cards_player.append(
                self.stack.stack_cards.pop())
        else:
            card = self.player.selected_card(command)
            is_valid_card = card.is_valid(self.stack.discard_cards)
            if is_valid_card is False:
                return "Your card is not valid"
            else:
                self.player.cards_player.remove(card)
                self.stack.put_card_in_discard(card)
                self.is_winner()

    def is_winner(self):
        if self.player.show_player_cards == []:
            self.is_playing = False
            return "You WON"

    def build_board(self):
        board = "Your cards are: \n"
        player_cards = self.player.show_player_cards()
        last_card_played = self.stack.show_last_card_played()
        for card in player_cards:
            board += card
            board += "\n"
        board += "The last card played is: \n" + last_card_played
        return board
