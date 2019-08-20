from .player import Player
from .turn import Turn
from . import (
    SETUP,
    GO,
    PLAYERS_QUANTITY_MESSAGE,
    PLAYING,
    FINISHED,
    PLAYER_CHOOSING_DICE_MESSAGE,
    PLAYER_DONE_MESSAGE,
    PLAYERS_NAME_MESSAGE,
    NEXT_PLAYER_TURN_MESSAGE,
    QUANTITY_SET,
    INVALID_NUMBER,
    PLAYERS_SET
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
        if self.state == SETUP:
            return PLAYERS_NAME_MESSAGE
        elif self.state == GO and self.actual_turn.is_playing():
            if self.actual_turn.plays[-1].is_playing:
                return PLAYER_CHOOSING_DICE_MESSAGE
            else:
                # innecesary?
                return PLAYER_DONE_MESSAGE
        elif self.state == GO and not self.actual_turn.is_playing():
            return NEXT_PLAYER_TURN_MESSAGE

    def next_player(self):
        self.who_is_playing = (self.who_is_playing + 1) \
            if self.who_is_playing in range(1, self.players_qty) else 1
        # import pdb; pdb.set_trace()
        self.actual_turn = Turn(self.players[self.who_is_playing - 1])

    def check_players_qty(self, players_qty):
        return False if players_qty == 0 else True

    # def validate_qty(self, response):
    #     if response not in list(range(1, 6)):
    #         raise NotCorrectPlayersQuantityException(INVALID_NUMBER)

    def create_players(self, names):
        for name in names:
            self.players.append(Player(name))
        self.players_qty = len(names)

    def play(self, player_input):

        if self.state == SETUP:
            names = player_input.split(',')
            self.state = GO
            self.create_players(names)
            self.next_player()
            return PLAYERS_SET
        elif player_input == 'STAY':
            # asignar puntaje
            self.actual_turn.calculate_acumulated_score()
            self.next_player()
        else:
            self.actual_turn.select_dices(player_input)
            if not self.actual_turn.is_playing():  # Loses the turn
                self.next_player()

    # Por cada jugador, mostrar su puntaje
    # @property
    # def board(self):
    #     return str(self.played_numbers)
