class DiezMil(object):  
    def __init__(self):
        self.players_qty = None
        self.base_score = None
        self.is_turn=True

    def next_turn(self):
        pass

    def set_players_qty(self, players_qty):
        self.players_qty = players_qty

    def check_players_qty(self, players_qty):
        if players_qty == 0:
            return False
        return True

