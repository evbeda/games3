from .room import Room


class Trap(Room):

    def __init__(self, effects):
        self.effects = effects

    def determine_affected_players(self):
        raise NotImplementedError("Can't be called")

    def resolve_room(self, hands):
        raise NotImplementedError("Can't be called")
