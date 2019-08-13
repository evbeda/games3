class Player:
    def __init__(self, name):
        self.name = name
        self.wounds = 0
        self.gold = 0

    def add_wounds(self, wounds):
        self.wounds += wounds

    def add_gold(self,gold):
        self.gold += gold
