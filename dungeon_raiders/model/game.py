from .level import Level
from ..model.__init__ import CHARACTER
from .player import Player
import random


class Game:
    def __init__(self):
        self.players = []
        self.create_players()
        self.create_levels()

    def create_levels(self):
        self.levels = [
            Level(self.players),
            Level(self.players),
            Level(self.players),
            Level(self.players),
            Level(self.players)
            ]

    def create_players(self):
        characters = []
        list_shuffle = list(range(0, 5))
        random.shuffle(list_shuffle)
        for k, v in enumerate(list_shuffle):
            characters.append(CHARACTER[v])
            self.players.append(Player('', characters[k]))
            if len(characters) == 3:
                break

    def get_winner(self):
        self.players.sort(key=lambda elem: elem.wounds)
        self.players.pop()
        self.players.sort(key=lambda elem: elem.gold, reverse=True)
        return self.players[0]

    def next_turn(self):
        pass    

    def play(self, number_card):

        pass

    @property
    def board(self):
        pass