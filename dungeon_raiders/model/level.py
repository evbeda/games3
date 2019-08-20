from .hand_player import HandPlayer


class Level:
    def __init__(self, players, number_level, deck):
        self.deck = deck
        self.number_level = number_level
        self.rooms = self.select_rooms()
        self.iter_rooms = iter(self.rooms)
        self.actual_room = next(self.iter_rooms)
        self.hands = self.create_hands_for_level(players)

    def __str__(self):
        msg = ', '
        room_names = [room.name for room in self.rooms]
        return f'Level:{self.number_level}\nRooms: {msg.join(room_names)}'

    def create_hands_for_level(self, players):
        return [HandPlayer(player) for player in players]

    def select_rooms(self):
        return [self.deck.pop() for i in range(5)]

    def execute_level(self, power_cards_played):
        [hand.play(power_cards_played[index])
            for index, hand in enumerate(self.hands)]
        self.actual_room.resolve_room(self.hands)
        self.actual_room = next(self.iter_rooms)
