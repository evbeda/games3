import unittest
from ..model.player import Player
from ..model.hand_player import HandPlayer


class RoomHelper(unittest.TestCase):
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
