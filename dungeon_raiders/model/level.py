from .hand_player import HandPlayer
from .hand_computer import HandComputer


class Level:
    def __init__(self, players, number_level, deck, level_card):
        self.index_actual_room = 0
        self.number_level = number_level
        self.rooms = self.select_rooms(deck)
        self.actual_room = self.rooms[self.index_actual_room]
        self.hands = self.create_hands_for_level(players)
        self.level_card = level_card

    def __str__(self):
        msg = ', '
        room_names = [room.name for room in self.rooms]
        return f'Level:{self.number_level}\nRooms: {msg.join(room_names)}'

    def create_hands_for_level(self, players):
        return [
            HandPlayer(players[0]),
            HandComputer(players[1]),
            HandComputer(players[2])
            ]

    def select_rooms(self, deck):
        return [deck.pop() for i in range(5)]

    def next_room(self):
        self.index_actual_room += 1

    def is_last_room(self):
        return self.index_actual_room == 4

    def execute_level(self, human_power_cards_played):
        self.hands[0].chosen_card = human_power_cards_played
        [hand.play()
            for index, hand in enumerate(self.hands)]
        self.actual_room.resolve_room(self.hands)
        self.actual_room = self.rooms[self.index_actual_room]
