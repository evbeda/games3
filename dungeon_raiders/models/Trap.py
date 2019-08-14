from .Room import Room

class Trap(Room):

    # trap_type = 'gold' / 'wounds'
    # effects = [0,0,1,2,2] (trampa de pinchos)
    #            1 2 3 4 5 (carta maxima jugada)
    def __init__(self, effects):
        self.effects = effects
    
    def determine_affected_players(self):
        raise NotImplementedError("Can't be called")

    def resolve_room(self, hands):
        raise NotImplementedError("Can't be called")

