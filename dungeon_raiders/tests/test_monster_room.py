from parameterized import parameterized
from . import RoomHelper
from ..model.rooms.monster_room import MonsterRoom


class TestMonsterRoom(RoomHelper):
    """ -------------------- MonsterRoom card --------------------"""
    @parameterized.expand([
        ([5, 3, 3, 5], MonsterRoom([14, 3, 'La Cosa']), [5, 3, 1, 2]),
        ([5, 3, 0, 5], MonsterRoom([14, 3, 'sad']), [5, 5, 4, 1]),
        ([5, 6, 3, 8], MonsterRoom([14, 3, 'gre']), [3, 2, 2, 2]),
    ])
    def test_play_check_wounds_against_monster_room(self, players_wounds,
                                                    monster, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(monster, plays)
        self.assertEqual(players_wounds, [
            handA.player.wounds,
            handB.player.wounds,
            handC.player.wounds,
            handD.player.wounds])
