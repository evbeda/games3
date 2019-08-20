from .player import Player
from . import (
    SETUP,
    GO,
    PLAYERS_QUANTITY_MESSAGE,
    PLAYING,
    FINISHED,
    PLAYER_CHOOSING_DICE_MESSAGE,
    PLAYER_DONE_MESSAGE,
    PLAYERS_NAME_MESSAGE,
    CHOOSING_DICE,
    NEXT_PLAYER_TURN_MESSAGE,
    QUANTITY_SET,
    INVALID_NUMBER,
)
from .exceptions.exceptions import (
    NotCorrectPlayersQuantityException,
)


class DiezMil(object):
    def __init__(self):
        self.state = SETUP
        self.players_qty = 0
        self.base_score = 0
        self.players = []
        self.who_is_playing = 0
        self.actual_turn = None

    # It's a circle, it adds one until the top boundary of players_qty
    # Otherwise it beging with the first one
    def next_turn(self):
        if self.state == SETUP and self.players_qty == 0:
            return PLAYERS_QUANTITY_MESSAGE
        elif self.state == SETUP and self.players_qty != 0:
            return PLAYERS_NAME_MESSAGE
        elif self.state == GO and self.actual_turn.state == PLAYING:
            if self.actual_turn.plays[-1] == CHOOSING_DICE:
                return PLAYER_CHOOSING_DICE_MESSAGE
            else:
                return PLAYER_DONE_MESSAGE
        elif self.state == GO and self.actual_turn == FINISHED:
            return NEXT_PLAYER_TURN_MESSAGE

    def next_player(self):
        if self.state == SETUP:
            self.who_is_playing = 1
            self.state = GO
        elif self.state == GO:
            self.who_is_playing = (self.who_is_playing + 1) \
                if self.who_is_playing in range(1, self.players_qty) else 1

    def check_players_qty(self, players_qty):
        return False if players_qty == 0 else True

    def validate_qty(self, response):
        if response not in list(range(1, 6)):
            raise NotCorrectPlayersQuantityException(INVALID_NUMBER)

    def create_players(self, names):
        for name in names:
            self.players.append(Player(name))

    def play(self, player_input):
        if self.state == SETUP and self.players_qty == 0:
            try:
                self.validate_qty(player_input)
            except NotCorrectPlayersQuantityException as e:
                return str(e)
            self.players_qty = player_input
            return QUANTITY_SET
        elif self.state == SETUP and self.players_qty != 0:
            names = player_input.split(',')
            self.create_players(names)

    # Por cada jugador, mostrar su puntaje
    @property
    def board(self):
        return str(self.played_numbers)
