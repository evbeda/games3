from parameterized import parameterized
from ..model import GOLDS, WOUNDS
from . import RoomHelper
from ..model.rooms.gold_room import GoldRoom
from ..model.rooms.wound_room import WoundRoom


class TestTrapRoom(RoomHelper):
    """ -------------------- GoldRoom card --------------------"""

    @parameterized.expand([
        ([4, 3, 0, 4], GoldRoom(GOLDS[0]), [3, 1, 2, 3]),
        ([3, 3, 0, 3], GoldRoom(GOLDS[0]), [4, 1, 2, 3]),
        ([2, 3, 0, 2], GoldRoom(GOLDS[0]), [5, 2, 3, 4]),
        ([4, 3, 0, 4], GoldRoom(GOLDS[1]), [2, 1, 2, 1]),
        ([4, 3, 0, 4], GoldRoom(GOLDS[1]), [3, 2, 1, 2]),
        ([3, 3, 0, 3], GoldRoom(GOLDS[1]), [4, 1, 3, 4]),
        ([3, 3, 0, 3], GoldRoom(GOLDS[1]), [5, 5, 4, 3]),
    ])
    def test_play_cards_against_gold_room(self, gold_values, room, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(room, plays)
        self.assertEqual(gold_values, [
                handA.player.gold, handB.player.gold, handC.player.gold,
                handD.player.gold])

    """ -------------------- WoundRoom card -------------------- """
    @parameterized.expand([
        ([5, 3, 1, 5], WoundRoom(WOUNDS[0]), [3, 1, 1, 2]),
        ([5, 3, 2, 5], WoundRoom(WOUNDS[0]), [4, 1, 2, 3]),
        ([5, 3, 2, 5], WoundRoom(WOUNDS[0]), [5, 2, 3, 4]),
        ([5, 3, 1, 5], WoundRoom(WOUNDS[1]), [2, 1, 1, 2]),
        ([5, 3, 1, 5], WoundRoom(WOUNDS[1]), [3, 1, 2, 3]),
        ([5, 3, 2, 5], WoundRoom(WOUNDS[1]), [4, 1, 2, 3]),
        ([5, 3, 2, 5], WoundRoom(WOUNDS[1]), [5, 2, 3, 4])
    ])
    def test_play_cards_against_wound_room(self, wound_values, room, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(room, plays)
        self.assertEqual(wound_values, [
            handA.player.wounds, handB.player.wounds, handC.player.wounds,
            handD.player.wounds])
