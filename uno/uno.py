from .stack import Stack
from .player import HumanPlayer, ComputerPlayer
from .exceptions import ComputerCantPlayException
from .const import (
    DRAW_CARD_INPUT,
    EXIT,
    EXIT_MESSAGE,
    INVALID_CARD_MESSAGE,
    ASK_FOR_INPUT,
    FINISHED_PLAY_MESSAGE
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
        self.actions = []

    def next_turn(self):
        if self.is_playing:
            return ASK_FOR_INPUT
        return 'Game Over, See you next time'

    def play(self, command):
        if command == EXIT:
            self.is_playing = False
            return EXIT_MESSAGE
        elif command == DRAW_CARD_INPUT:
            self.player_passes()
            return ''
        else:
            card_index, color = self.parse_command(command)
            try:
                card_played = self.current_player.select_card(
                    card_index, self.stack)
            except Exception:
                return INVALID_CARD_MESSAGE
            # Duplicated
            self.actions.append('You played {}'.format(card_played))
            self.stack.put_card_in_discard(card_played)
            loses_turn, cards_to_pick = card_played.get_action()
            if self.is_winner():
                self.is_playing = False
                return '{} won!'.format(self.current_player)
            self.current_player = self.decide_whos_next(loses_turn)
            while self.current_player == self.computer_player:
                try:
                    card_played = self.current_player.select_card(self.stack)
                except ComputerCantPlayException:
                    self.player_passes()
                # Duplicated
                self.actions.append('Computer played {}'.format(card_played))
                self.stack.put_card_in_discard(card_played)
                loses_turn, cards_to_pick = card_played.get_action()
                if self.is_winner():
                    self.is_playing = False
                    return '{} won!'.format(self.current_player)
                self.current_player = self.decide_whos_next(loses_turn)
            return FINISHED_PLAY_MESSAGE

    def player_passes(self):
        if self.current_player.has_drawn_a_card:
            self.current_player.has_drawn_a_card = False
            self.current_player = self.decide_whos_next(False)
        else:
            self.player_draws(self.current_player)

    def player_draws(self, player):
        player.cards_player.append(self.stack.draw_card_from_stack())
        player.has_drawn_a_card = True

    def is_winner(self):
        return self.current_player.cards_player == []

    @property
    def board(self):
        board = "Your cards are:\n"
        player_cards = self.player.cards_player
        last_card_played = self.stack.discard_cards[-1]
        computer_remaining_cards = len(self.computer_player.cards_player)
        # for index, card in enumerate(player_cards):
        #     board += str(index + 1) + ': ' + str(card)
        #     board += "\n"
        board += '\n'.join(
            [str(index + 1) + ': ' + str(card)
                for index, card in enumerate(player_cards)]
            ) + '\n'
        board += \
            f'Computer remaining cards: {computer_remaining_cards}\n'
        board += "The last card played is:\n" + str(last_card_played)
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

