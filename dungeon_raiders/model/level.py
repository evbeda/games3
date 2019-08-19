from random import choice, randint
from .__init__ import MONSTER_ROOM, MONSTERS, TREASURES, TREASURE_ROOM, \
                        GOLDS, GOLD_TRAP_ROOM, WOUNDS
from .rooms.monster_room import MonsterRoom
from .rooms.treasure import Treasure
from .rooms.gold_room import GoldRoom
from .rooms.wound_room import WoundRoom
from .hand_player_state import HandPlayerState


class Level:
    def __init__(self, players):
        self.rooms = []
        self.hands = []
        self.create_hands_for_level(players)
        self.select_room()

    def create_hands_for_level(self, players):
        for player in players:
            self.hands.append(HandPlayerState(player))

    def select_room(self):
        for i in range(5):
            number_room = randint(0, 3)
            if number_room == MONSTER_ROOM:
                self.rooms.append(MonsterRoom(choice(MONSTERS)))
            elif number_room == TREASURE_ROOM:
                self.rooms.append(Treasure(choice(TREASURES)))
            elif number_room == GOLD_TRAP_ROOM:
                self.rooms.append(GoldRoom(choice(GOLDS)))
            else:
                self.rooms.append(WoundRoom(choice(WOUNDS)))