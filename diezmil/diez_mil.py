class DiezMil(object):
    def __init__(self):
        self.players_qty = 0
        self.base_score = 0
        self.players = []

    # Es ciclico, devolver desde una lista de jugadores el siguiente
    def next_turn(self):
        pass

    # Metodo de creacion de jugadores

    def set_players_qty(self, players_qty):
        self.players_qty = players_qty

    def check_players_qty(self, players_qty):
        return False if players_qty == 0 else True

    def play(self):

        # Preguntar la cantidad de jugadores

        # Crear los jugadores

        # Por cada jugador, crear un turno y que empiecen las apuestas
        pass

    # Por cada jugador, mostrar su puntaje
    @property
    def board(self):
        return str(self.played_numbers)
