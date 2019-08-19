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

    def resolve_game(self):
        finalists = self.get_finalists()
        winners = self.get_players_with_max_gold(finalists)
        if len(winners) == len(self.get_players_with_max_wounds(winners)):
            return winners
        return [player for player in winners
                if player not in self.get_players_with_max_wounds(winners)]

    def get_finalists(self):
        players_with_max_wound = self.get_players_with_max_wounds(self.players)
        if len(self.players) - len(players_with_max_wound) < 2:
            return self.players
        return [player for player in self.players
                if player not in players_with_max_wound]

    def get_players_with_max_wounds(self, players):
        max_wounds_value = max([player.wounds for player in players])
        return [player for player in players
                if player.wounds == max_wounds_value]

    def get_players_with_max_gold(self, players):
        max_gold_value = max([player.gold for player in players])
        return [player for player in players
                if player.gold == max_gold_value]

    def next_turn(self):
        pass

    def play(self, command):
        if command == EXIT:
            self.is_playing = False

    @property
    def board(self):
        pass
