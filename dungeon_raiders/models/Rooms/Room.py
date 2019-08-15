

class Room:

    def __init__(self, name):
        self.name = name

    def resolve_room(self, hands):
        raise NotImplementedError("Can't be called")
