from .level import Level
from . import CHARACTER, EXIT, ROOMS, LEVEL_CARDS
from .player import Player
import random


class Game:
    input_args = 1

    def __init__(self):
        self.is_playing = True
        self.players = self.create_players()
        self.levels = self.create_levels()
        self.current_level = self.levels[0]

    def create_levels(self):
        deck = ROOMS.copy()
        level_cards = LEVEL_CARDS.copy()
        random.shuffle(deck)
        random.shuffle(level_cards)
        return [
                Level(self.players, i+1, deck, random.choice(level_cards))
                for i in range(5)
        ]

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
        msg = ''
        if self.is_playing is True:
            msg += f"{self.current_level.actual_room.__str__()}"
        else:
            msg += 'Bye'
        return msg

    def play(self, *command):
        if command[0] == EXIT:
            self.is_playing = False
            return 'bye'
        else:
            pass
            # number_played = command[0]
            # self.actual_level.execute_level([number_played, random, random])

    @property
    def board(self):
        msg = f"{self.current_level.__str__()}\n"
        msg += '\n'.join(
            [f'{player.character}, wounds:{player.wounds}, gold:{player.gold}'
                for player in self.players]
            )
        return msg
