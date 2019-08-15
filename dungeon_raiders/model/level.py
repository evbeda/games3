from .rooms.room import Room
from .hand_player_state import HandPlayerState


class Level:
    def __init__(self, players):
        self.rooms = [
            Room('Monster'),
            Room('Treasure'),
            Room('GoldTrap'),
            Room('WoundTrap'),
            Room('Moster')
        ]
        self.hands = []

        for player in players:
            self.hands.append(HandPlayerState(player))
