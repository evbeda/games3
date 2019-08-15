from .handplayerstate import HandPlayerState


class Level:
    def __init__(self, players):
        self.room = []
        self.hands = []
        for player in players:
            self.hands.append(HandPlayerState(player))
