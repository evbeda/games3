# Modules
from parameterized import parameterized
from random import choice
from unittest.mock import patch
# Model
from ..model.level import Level
from ..model import ROOMS, LEVEL_CARDS, MONSTERS, GOLDS, TREASURES, WOUNDS
from ..model.rooms.monster_room import MonsterRoom
from ..model.rooms.treasure import Treasure
from ..model.rooms.gold_room import GoldRoom
from ..model.rooms.wound_room import WoundRoom
# Helpers
from . import RoomHelper


class TestLevel(RoomHelper):
    def setUp(self):
        self.players = self._get_players_example()
        self.deck = ROOMS.copy()
        self.level = Level(self.players, 1, self.deck, choice(LEVEL_CARDS))

    def test_check_if_each_levels_has_five_rooms(self):
        self.assertEqual(5, len(self.level.rooms))

    def test_create_hands_for_level(self):
        result = self.level.create_hands_for_level(self.players)
        self.assertEqual(self.players, [hand.player for hand in result])

    def test_select_rooms_use_different_rooms_for_each_level(self):
        deck = ROOMS.copy()
        levels = [
            Level(self.players, i, deck, choice(LEVEL_CARDS))
            for i in range(5)
        ]
        rooms = [room for level in levels for room in level.rooms]
        for room in rooms:
            self.assertEqual(rooms.count(room), 1)
            self.assertNotIn(room, deck)

    def test_level_has_a_level_card(self):
        deck = ROOMS.copy()
        levels = [
            Level(self.players, i, deck, choice(LEVEL_CARDS))
            for i in range(5)
        ]
        for level in levels:
            self.assertIn(level.level_card, LEVEL_CARDS)

# PLAYERS_EXAMPLE = [             wounds, gold
#    Player(character=['Caballero', 1, 1]),
#    Player(character=['Exploradora', 3, 2]),
#    Player(character=['Guerrero', 2, 0]),
# ]
    @parameterized.expand([
        ([1, 4, 5], 0, 'wounds', MonsterRoom((11, 3, 'Esqueleto')), 4),
        ([3, 2, 3], 0, 'gold', Treasure((4, 2)), 3),
        ([3, 2, 3], 2, 'gold', Treasure((4, 2)), 2)
    ])
    def test_execute_level(
            self, cards_played, player_affected,
            attribute_affected, actual_room, expected_effect
            ):
        level = Level(self.players, 1, ROOMS[:], choice(LEVEL_CARDS))
        level.actual_room = actual_room
        with patch(
            'dungeon_raiders.model.hand_computer.choice',
            side_effect=(cards_played[1], cards_played[2])
        ):
            level.execute_level(cards_played[0])
            self.assertEqual(
                getattr(self.players[player_affected], attribute_affected),
                expected_effect
                )

    def test_level_to_string(self):
        level = Level(self.players, 2, self.deck, LEVEL_CARDS[6])
        level.rooms = [
            MonsterRoom(MONSTERS[1]),
            Treasure(TREASURES[3]),
            WoundRoom(WOUNDS[0]),
            MonsterRoom(MONSTERS[5]),
            GoldRoom(GOLDS[0])
            ]
        level.index_actual_room = 2
        expected = "Level: 2\n"
        expected += "Rooms:\n"
        expected += " * Esqueleto (❤️ 11, 🗡️️ 3)\n"
        expected += " * Treasure (💰 3, 💰 2)\n"
        expected += " * Trampa de pinchos <--\n"
        expected += " * Hidden\n"
        expected += " * Caldero de lava"
        self.assertEqual(str(level), expected)
