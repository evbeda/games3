class Game:
    def __init__(self, players):
        self.players = players

    def get_winner(self):
        self.players.sort(key=lambda elem: elem.wounds)
        self.players.pop()
        self.players.sort(key=lambda elem: elem.gold, reverse=True)
        return self.players[0]
