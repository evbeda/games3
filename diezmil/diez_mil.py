from .player import Player
from .turn import Turn
from .__init__ import SETUP, GO
from .exceptions.exceptions import NegativePlayersQuantityException, \
    NullPlayersQuantityException, DifferentPlayerQuantityAndNamesException, \
    ManyPlayersQuantityException, NotCorrectPlayersQuantityException, \
    NotANumberException


class DiezMil(object):
    def __init__(self):
        self.state = SETUP
        self.players_qty = 0
        self.base_score = 0
        self.players = []
        self.who_is_playing = 0
        self.actual_turn = []

    # It's a circle, it adds one until the top boundary of players_qty
    # Otherwise it beging with the first one
    def next_player(self):
        if self.state == SETUP:
            self.who_is_playing = 1
            self.state = GO
        elif self.state == GO:
            self.who_is_playing = (self.who_is_playing + 1) \
                if self.who_is_playing in range(1, self.players_qty) else 1

    def players_creator(self, players_quantity, names):
        if players_quantity < 0:
            raise NegativePlayersQuantityException
        elif players_quantity == 0:
            raise NullPlayersQuantityException
        elif players_quantity >= 6:
            raise ManyPlayersQuantityException
        elif players_quantity in list(range(1, 6)):
            if len(names) == players_quantity:
                for name in names:
                    self.players.append(Player(name))
            else:
                raise DifferentPlayerQuantityAndNamesException
        return self.players

    def check_players_qty(self, players_qty):
        return False if players_qty == 0 else True

    def ask_for_players_quantity(self):
        asking_ended = False
        while asking_ended is False:
            response = input("How many players?: (A number between 1 and 5) ")
            possible_quantity = 0
            try:
                possible_quantity = int(response)
            except ValueError:
                raise NotANumberException()
            if possible_quantity in list(range(1, 6)):
                self.set_players_qty(possible_quantity)
                asking_ended = True
            else:
                raise NotCorrectPlayersQuantityException()

    def create_players(self):
        for i in list(range(1, self.players_qty + 1)):
            name = input("What's the name of player " + str(i))
            self.players.append(Player(name))

    def play(self, command):
        if self.state == SETUP:
            # Ask for players's quantity
            self.ask_for_players_quantity()
            # Create players
            self.create_players()
            # Who's next?
            self.next_turn()
        elif self.state == GO:
            # Crear un turno para el jugador y que empiecen las apuestas
            if self.actual_turn:
                self.actual_turn = Turn(self.players[self.who_is_playing])

            command = self.resolve_command(command)
            self.actual_turn.generate_play()

            # El primer jugador jugo pero no termino
            # El primer jugador decide terminar
            # Comienza el siguiente jugador

    # Por cada jugador, mostrar su puntaje
    @property
    def board(self):
        return str(self.played_numbers)
