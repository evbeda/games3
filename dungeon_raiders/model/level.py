from random import sample
from . import ROOMS
from .hand_player import HandPlayer


class Level:
    def __init__(self, players):
        self.rooms = self.select_rooms()
        self.hands = self.create_hands_for_level(players)

    def create_hands_for_level(self, players):
        return [HandPlayer(player) for player in players]

    def select_rooms(self):
        return sample(ROOMS, k=5)
