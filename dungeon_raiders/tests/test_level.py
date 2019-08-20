import unittest
from ..model.level import Level
from ..model.player import Player


class TestLevel(unittest.TestCase):
    def test_check_if_each_levels_has_five_rooms(self):
        level = Level([Player('A'), Player('B'), Player('C')])
        self.assertEqual(5, len(level.rooms))


