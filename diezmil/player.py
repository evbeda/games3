

class Player:

    def __init__(self, name):
        self.name = name
        self.actual_score = 0

    def __gt__(self, player):
        return self.name == player.name and \
            self.actual_score == player.actual_score
