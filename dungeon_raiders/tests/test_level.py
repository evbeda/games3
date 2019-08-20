import unittest
from ..model.level import Level
from ..model.player import Player
from ..model import ROOMS


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player('A'),
            Player('B'),
            Player('C'),
        ]
        self.deck = ROOMS.copy()
        self.level = Level(self.players, 1, self.deck)

    def test_check_if_each_levels_has_five_rooms(self):
        self.assertEqual(5, len(self.level.rooms))

    def test_create_hands_for_level(self):
        result = self.level.create_hands_for_level(self.players)
        self.assertEqual(self.players, [hand.player for hand in result])

    def test_select_rooms(self):
        # TODO: refactor room deck handling
        pass
