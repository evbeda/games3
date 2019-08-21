# Modules
from parameterized import parameterized
from random import choice
# Model
from ..model.level import Level
from ..model import ROOMS, LEVEL_CARDS
from ..model.rooms.monster_room import MonsterRoom
from ..model.rooms.treasure import Treasure
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
        self, cards_played, player_affected, attribute_affected, actual_room, expected_effect
            ):
        level = Level(self.players, 1, ROOMS[:], choice(LEVEL_CARDS))
        level.actual_room = actual_room
        level.execute_level(cards_played)
        self.assertEqual(
            getattr(self.players[player_affected], attribute_affected), expected_effect)
