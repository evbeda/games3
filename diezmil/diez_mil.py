from .player import Player
from .turn import Turn
from . import (
    SETUP,
    GO,
    PLAYER_CHOOSING_DICE_MESSAGE,
    PLAYER_DONE_MESSAGE,
    PLAYERS_NAME_MESSAGE,
    NEXT_PLAYER_TURN_MESSAGE,
    PLAYERS_SET,
    CANT_SAVE_THOSE_DICES,
)
from .exceptions.exceptions import (
    PlayRemainsWithNoScore,
    InvalidSelectedDices
)


class DiezMil(object):

    name = 'Diezmil Game'
    input_args = 1

    def __init__(self):
        self.is_playing = True
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
            ret = self.actual_turn.calculate_acumulated_score()
            if self.actual_turn.is_player_win():
                self.is_playing = False
                return 'Player win: ' + self.actual_turn.player.name
            self.next_player()
            return ret
        else:
            selected_dices = DiezMil.parse_input(player_input)
            try:
                self.actual_turn.select_dices(selected_dices)
                if not self.actual_turn.is_playing():
                    self.next_player()
            except (PlayRemainsWithNoScore):
                return CANT_SAVE_THOSE_DICES

    @staticmethod
    def parse_input(user_input):
        parsed = user_input.split(",")
        parsed = [int(x) for x in parsed]
        return parsed

    # Por cada jugador, mostrar su puntaje
    @property
    def board(self):
        board = ""
        if self.actual_turn:
            board += self.actual_turn.build_board()
        return board
