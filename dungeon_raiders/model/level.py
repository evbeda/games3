from random import sample
from . import ROOMS
from .hand_player import HandPlayer


class Level:
    def __init__(self, players, number_level):
        self.number_level = number_level
        self.rooms = self.select_rooms()
        self.hands = self.create_hands_for_level(players)

    def __str__(self):
        msg = ', '
        room_names = [room.name for room in self.rooms]
        return f'Level:{self.number_level}\nRooms: {msg.join(room_names)}'

    def create_hands_for_level(self, players):
        return [HandPlayer(player) for player in players]

    def select_rooms(self):
        return sample(ROOMS, k=5)
