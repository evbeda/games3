from .level import Level
from . import CHARACTER, EXIT
from .player import Player
import random


class Game:
    def __init__(self):
        self.is_playing = True
        self.players = self.create_players()
        self.levels = self.create_levels()
        self.current_level = self.levels[0]

    def create_levels(self):
        return [Level(self.players) for i in range(5)]

    def create_players(self):
        players = [Player(character=c) for c in random.sample(CHARACTER, k=3)]
        return players

    def get_winner(self):
        self.players.sort(key=lambda elem: elem.wounds)
        self.players.pop()
        self.players.sort(key=lambda elem: elem.gold, reverse=True)
        return self.players[0]

    def next_turn(self):
        pass

    def play(self, command):
        if command == EXIT:
            self.is_playing = False

    @property
    def board(self):
        pass
