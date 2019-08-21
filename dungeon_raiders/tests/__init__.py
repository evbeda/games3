import unittest
from ..model.player import Player
from ..model.hand_player import HandPlayer
from ..model.rooms.monster_room import MonsterRoom
from ..model.rooms.treasure import Treasure
from ..model.rooms.gold_room import GoldRoom


BOARD_EXAMPLE = '''Level:1
Rooms: Esqueleto, Treasure, Caldero de lava, Dragon, Treasure
Caballero, wounds:1, gold:1
Exploradora, wounds:3, gold:2
Guerrero, wounds:2, gold:0'''

NEXT_TURN_WOUNDROOM_EXAMPLE = '''Room name: Trampa de pinchos
Card: 5 Wound: 2
Card: 4 Wound: 2
Card: 3 Wound: 1
'''

NEXT_TURN_TREASURE_EXAMPLE = '''Room name: Treasure
First winner: 4
Second winner: 2
'''

NEXT_TURN_GOLDROOM_EXAMPLE = '''Room name: Caldero de lava
Max played: 5 Gold: 3
Max played: 4 Gold: 2
Max played: 3 Gold: 1
'''

NEXT_TURN_MONSTERROOM_EXAMPLE = '''Room name: Esqueleto
Life: 11
Damage: 3
'''

ROOMS_EXAMPLE = [
    MonsterRoom((11, 3, 'Esqueleto')),
    Treasure((4, 2)),
    GoldRoom(['Caldero de lava', [(5, 3), (4, 2), (3, 1)]]),
    MonsterRoom((14, 3, 'Dragon')),
    Treasure((3, 2)),
]

PLAYERS_EXAMPLE = [
            Player(character=['Caballero', 1, 1]),
            Player(character=['Exploradora', 3, 2]),
            Player(character=['Guerrero', 2, 0]),
        ]


class RoomHelper(unittest.TestCase):
    def _get_players_example(self):
        return[
            Player(character=['Caballero', 1, 1]),
            Player(character=['Exploradora', 3, 2]),
            Player(character=['Guerrero', 2, 0]),
        ]

    def _get_hands(self):

        player_a = Player('A')
        player_a.add_gold(5)
        player_a.add_wounds(5)
        player_b = Player('B')
        player_b.add_gold(3)
        player_b.add_wounds(3)
        player_c = Player('C')
        player_c.add_gold(0)
        player_c.add_wounds(0)
        player_d = Player('D')
        player_d.add_gold(5)
        player_d.add_wounds(5)

        return HandPlayer(player_a), HandPlayer(player_b), \
            HandPlayer(player_c), HandPlayer(player_d)

    def _play_cards_against_room(self, room, plays):
        hands = self._get_hands()

        for hand in hands:
            hand.play(plays[hands.index(hand)])
        return self._play(room, hands)

    def _play(self, room, hands):
        room.resolve_room(hands)
        return hands
