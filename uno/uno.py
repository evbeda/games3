# Model
from .stack import Stack
from .player import HumanPlayer, ComputerPlayer
# Exception
# from .exceptions import ComputerCantPlayException
# Const
from .const import (
    # Commands
    DRAW_CARD_INPUT, EXIT,
    # Messages
    INVALID_CARD_MESSAGE,
    ASK_FOR_INPUT,
    COMPUTER_WON_MESSAGE,
    HUMAN_PLAYER_WON_MESSAGE
    )


class Uno():

    name = 'Uno Game'
    input_args = 1

    def __init__(self):
        self.is_playing = True
        self.stack = Stack()
        self.player = HumanPlayer(self.stack.generate_cards_player())
        self.computer_player = ComputerPlayer(
            self.stack.generate_cards_player())
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
            self.player_passes()
        else:
            card_index, color = self.parse_command(command)
            try:
                card_played = self.current_player.select_card(
                    card_index, self.stack
                    )
                self.stack.put_card_in_discard(card_played)
                loses_turn, cards_to_pick = \
                    card_played.get_action()
                self.current_player = \
                    self.decide_whos_next(loses_turn)
            except Exception:
                return INVALID_CARD_MESSAGE
            # except ComputerCantPlayException:
            #     self.player_passes()

    def player_passes(self):
        if self.current_player.has_drawn_a_card:
            self.current_player.has_drawn_a_card = False
            self.current_player = self.decide_whos_next(False)
        else:
            self.player_draws(self.current_player)

    def player_draws(self, player):
        player.cards_player.append(self.stack.draw_card_from_stack())
        player.has_drawn_a_card = True

    def winner(self):
        if self.player.cards_player == []:
            self.is_playing = False
            return HUMAN_PLAYER_WON_MESSAGE
        elif self.computer_player.cards_player == []:
            self.is_playing = False
            return COMPUTER_WON_MESSAGE

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
            return self.current_player
        else:
            if self.current_player == self.computer_player:
                return self.player
            else:
                return self.computer_player
