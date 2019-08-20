from .const import DRAW_CARD_INPUT, EXIT
from .stack import Stack
from .player import Player
from .const import ASK_FOR_INPUT


class Uno():

    name = 'Uno Game'
    input_args = 1

    def __init__(self):
        self.is_playing = True
        self.stack = Stack()
        self.player = Player(self.stack.generate_cards_player())
        self.computer_player = Player(
            self.stack.generate_cards_player(),
            'Computer_player'
            )
        self.stack.put_card_in_discard()

    def next_turn(self):
        if self.is_playing:
            return ASK_FOR_INPUT
        return 'Game Over, See you next time'

    def play(self, command):
        if not self.player.loses_turn:
            if command == EXIT:
                self.is_playing = False
                return 'Bye'
            elif command == DRAW_CARD_INPUT:
                return self.player.cards_player.append(
                    self.stack.stack_cards.pop())
            else:
                card = self.player.selected_card(command)
                is_valid_card = card.is_valid(self.stack.discard_cards[-1])
                if is_valid_card is False:
                    return "Your card is not valid"
                else:
                    self.player.cards_player.remove(card)
                    self.stack.put_card_in_discard(card)
                    # Get card action. Maybe put in other function
                    lose_turn, cards_to_pick = card.get_action()
                    if lose_turn:
                        self.computer_player.loses_turn = True
                    return self.winner(self.player)
        if not self.computer_player.loses_turn:
            card = self.computer_player.auto_play(self.stack.discard_cards[-1])
            if card is not None:
                self.stack.put_card_in_discard(card)
                return self.winner(self.computer_player)
            else:
                return self.computer_player.cards_player.append(
                    self.stack.stack_cards.pop())

    def winner(self, player):
        if player.cards_player == []:
            self.is_playing = False
            return "You WON" if player.name == 'Player' else 'Computer WON'

    @property
    def board(self):
        board = "Your cards are: \n"
        player_cards = self.player.cards_player
        last_card_played = self.stack.discard_cards[-1]
        for index, card in enumerate(player_cards):
            board += str(index + 1) + ': ' + str(card)
            board += "\n"
        board += "The last card played is: \n" + str(last_card_played)
        return board
