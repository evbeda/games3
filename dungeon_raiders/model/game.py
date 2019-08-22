# Modules
import random
# Model
from .level import Level
from .player import Player
# Messages
from . import (
    CHARACTER,
    EXIT,
    ROOMS,
    BYE_MESSAGE,
    ROOM_MESSAGE,
    GAME_OVER,
    LEVEL_FINISHED_MESSAGE,
    LEVEL_CARDS
    )


class Game:
    name = 'Dungeon Raiders'
    input_args = 1

    def __init__(self):
        self.index_current_level = 0
        self.is_playing = True
        self.players = self.create_players()
        self.levels = self.create_levels()
        self.current_level = self.levels[self.index_current_level]

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
            return BYE_MESSAGE
        else:
            try:
                power_card_played = command[0]
                self.current_level.execute_level(power_card_played)
                if self.current_level.is_last_room():
                    self.index_current_level += 1
                    self.current_level = self.levels[self.index_current_level]
                    return LEVEL_FINISHED_MESSAGE
                self.current_level.next_room()
                return ROOM_MESSAGE
            except IndexError:
                self.is_playing = False
                return GAME_OVER
            except Exception as e:
                return str(e)

    @property
    def board(self):
        if self.is_playing is True:
            msg = f"{self.current_level.__str__()}\n"
            msg += '\n'.join(
                [f'{player.character}, wounds:{player.wounds}, gold:{player.gold}'
                    for player in self.players]
                )
        else:
            msg = f'Game over\n'
            winners = self.resolve_game()
            msg += f'Winners:\n' if len(winners) > 1 else f'Winner:\n'
            msg += '\n'.join(
                [f'{winner.character}, wounds:{winner.wounds}, gold:{winner.gold}'
                    for winner in winners]
            )
        return msg
