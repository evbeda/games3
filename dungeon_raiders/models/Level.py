from .Rooms.Room import Room
from .HandPlayerState import HandPlayerState


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
