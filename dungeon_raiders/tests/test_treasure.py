from parameterized import parameterized
from ..model.rooms.treasure import Treasure
from . import RoomHelper


class TestTreasure(RoomHelper):
    """ -------------------- Treasure card --------------------"""
    ''' Player A has 5 gold
        Player B has 3 gold
        Player C has 0 gold
        Player D has 5 gold
        '''
    @parameterized.expand([
        ([9, 5, 0, 5], Treasure([4, 2]), [5, 3, 1, 1]),
        ([7, 5, 1, 5], Treasure([4, 1]), [5, 5, 4, 1]),
        ([8, 3, 0, 5], Treasure([3, 0]), [3, 2, 2, 1])
    ])
    def test_play_check_who_win_treasure(
            self, players_gold_win, treasure, plays):
        hands, result = self._play_cards_against_room(treasure, plays)
        self.assertEqual(players_gold_win, [hand.player.gold for hand in hands])

    @parameterized.expand([
        ("Caballero earnt 3 gold.",
            Treasure([3, 0]), [3, 2, 2, 2]),
        ("Caballero and Exploradora earnt 1 gold.",
            Treasure([3, 0]), [3, 3, 2, 2]),
        ("Caballero, Exploradora and Guerrero earnt 1 gold.",
            Treasure([3, 0]), [3, 3, 3, 2]),
        ("Caballero, Exploradora, Guerrero and Hechicero earnt 0 gold.",
            Treasure([3, 0]), [2, 2, 2, 2]),
        ("Caballero earnt 4 gold. Exploradora earnt 2 gold.",
            Treasure([4, 2]), [5, 3, 1, 2]),
        ("Caballero earnt 4 gold. Exploradora and Guerrero earnt 1 gold.",
            Treasure([4, 2]), [5, 4, 4, 1]),
        ("Caballero earnt 4 gold. Exploradora, Guerrero and Hechicero earnt 0 gold.",
            Treasure([4, 2]), [5, 4, 4, 4]),
    ])
    def test_return_resolve_room(self, expected, treasure, plays):
        hands, result = self._play_cards_against_room(treasure, plays)
        self.assertEqual(expected, result)
