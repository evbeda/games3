from .const import DRAW_CARD_INPUT, EXIT, INVALID_CARD_MESSAGE
from .stack import Stack
from .player import HumanPlayer, Player
from .const import ASK_FOR_INPUT


class Uno():

    name = 'Uno Game'
    input_args = 1

    def __init__(self):
        self.is_playing = True
        self.stack = Stack()
        self.player = HumanPlayer(self.stack.generate_cards_player())
        self.computer_player = Player(self.stack.generate_cards_player())
        self.stack.put_card_in_discard()
        self.current_player = self.player

    def next_turn(self):
        if self.is_playing:
            return ASK_FOR_INPUT
        return 'Game Over, See you next time'

    def play(self, command):
        if command == EXIT:
            self.is_playing = False
        elif command == DRAW_CARD_INPUT:
            if self.player.already_take_a_card:
                self.current_player = self.decide_whos_next(True)
                self.player.already_take_a_card = False
            else:
                self.player_draws(self.player)
        else:
            card_index, color = self.parse_command(command)
            try:
                card_played = self.current_player.play(card_index, self.stack)
            except Exception:
                return INVALID_CARD_MESSAGE

    def player_draws(self, player):
        player.cards_player.append(self.stack.draw_card_from_stack())
        player.already_take_a_card = True

    def player_plays_card(self, player, card):
        player.cards_player.remove(card)
        self.stack.put_card_in_discard(card)

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

    def parse_command(self, command):
        color = None
        split = command.split()
        card_index = int(split[0]) - 1
        if len(split) == 2:
            color = split[1]
        return (card_index, color)

    def decide_whos_next(self, loses_turn):
        if loses_turn:
            if self.current_player == self.computer_player:
                return self.player
            else:
                return self.computer_player
        else:
            return self.current_player
