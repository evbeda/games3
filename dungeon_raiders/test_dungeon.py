import unittest
from .models.player import Player
from .models.handplayerstate import HandPlayerState
from .models.game import Game
from .models.rooms.monsterroom import MonsterRoom
from .models.rooms.goldroom import GoldRoom
from .models.rooms.woundroom import WoundRoom
from .models.rooms.treasure import Treasure
from parameterized import parameterized
from .models.exceptions.UnplayableCardException import UnplayableCardException


class TestDungeon(unittest.TestCase):

    """ -------------------- Player tests -------------------- """
    def test_init_hand(self):
        hand = HandPlayerState(Player('A'))
        self.assertEqual(5, len(hand.cards_to_play))

    def test_check_if_player_can_play_card_2(self):
        hand = HandPlayerState(Player('A'))
        hand.play(2)
        hand.play(5)
        with self.assertRaises(UnplayableCardException):
            hand.play(2)

    def test_check_actual_card(self):
        hand = HandPlayerState(Player('A'))
        hand.play(2)
        self.assertEqual(2, hand.last_card_played)

    def test_check_if_3_is_in_hand(self):
        hand = HandPlayerState(Player('A'))
        hand.play(3)
        self.assertTrue(3 not in hand.cards_to_play)

    """ -------------------- Game tests -------------------- """
    def test_check_if_game_has_5_levels(self):
        game = Game([Player('A'), Player('B')])
        self.assertEqual(5, len(game.levels))

    def test_check_if_player_a_wins(self):
        playerA = Player('A')
        playerB = Player('B')
        playerC = Player('C')
        playerA.gold = 50
        playerA.wounds = 10
        playerB.gold = 40
        playerB.wounds = 15
        playerC.gold = 60
        playerC.wounds = 20
        game = Game([playerA, playerB, playerC])
        self.assertEqual(playerA, game.get_winner())

    def _play(self, room, hands):
        room.resolve_room(hands)
        return hands


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

        return HandPlayerState(player_a), HandPlayerState(player_b), \
            HandPlayerState(player_c), HandPlayerState(player_d)

    def _play_cards_against_room(self, room, plays):
        hands = self._get_hands()

        for hand in hands:
            hand.play(plays[hands.index(hand)])
        return self._play(room, hands)

    def _play(self, room, hands):
        room.resolve_room(hands)
        return hands


class TestMonsterRoom(RoomHelper):

    """ -------------------- MonsterRoom card --------------------"""
    @parameterized.expand([
        ([5, 3, 3, 5], MonsterRoom(14, 3), [5, 3, 1, 2]),
        ([5, 3, 0, 5], MonsterRoom(14, 3), [5, 5, 4, 1]),
        ([5, 6, 3, 8], MonsterRoom(14, 3), [3, 2, 2, 2]),
    ])
    def test_play_check_wounds_against_monster_room(self, players_wounds, monster, plays):
        handA, handB, handC, handD = \
            super()._play_cards_against_room(monster, plays)
        self.assertEqual(players_wounds, [
            handA.player.wounds,
            handB.player.wounds,
            handC.player.wounds,
            handD.player.wounds])


class TestTrapRoom(RoomHelper):
    """ -------------------- GoldRoom card --------------------"""

    @parameterized.expand([
        ([3, 3, 0, 3], GoldRoom([0, 0, 1, 2, 3]), [3, 2, 4, 4]),
        ([5, 3, 0, 5], GoldRoom([0, 0, 1, 2, 3]), [1, 1, 1, 1]),
        ([2, 3, 0, 2], GoldRoom([0, 0, 1, 2, 3]), [5, 5, 5, 5])
    ])
    def test_play_cards_against_gold_room(self, gold_values, room, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(room, plays)
        self.assertEqual(gold_values, [
                handA.player.gold, handB.player.gold, handC.player.gold,
                handD.player.gold])

    """ -------------------- WoundRoom card -------------------- """
    @parameterized.expand([
        ([5, 3, 2, 5], WoundRoom([0, 0, 1, 2, 2]), [3, 2, 4, 4]),
        ([5, 3, 0, 5], WoundRoom([0, 0, 1, 2, 2]), [1, 2, 2, 1]),
        ([5, 3, 2, 5], WoundRoom([0, 0, 1, 2, 2]), [5, 4, 3, 2]),
    ])
    def test_play_cards_against_wound_room(self, wound_values, room, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(room, plays)
        self.assertEqual(wound_values, [
            handA.player.wounds, handB.player.wounds, handC.player.wounds,
            handD.player.wounds])


class TestTreasure(RoomHelper):
    """ -------------------- Treasure card --------------------"""
    ''' Player A has 5 gold
        Player B has 3 gold
        Player C has 0 gold
        Player D has 5 gold
        '''
    # If you have 2 treasures, evaluates 2 rewards.
    # If you only have 1 treasure, the second value is 0

    @parameterized.expand([
        ([9, 5, 0, 5], Treasure([4, 2]), [5, 3, 1, 1]),
        ([7, 5, 1, 5], Treasure([4, 1]), [5, 5, 4, 1]),
        ([8, 3, 0, 5], Treasure([3, 0]), [3, 2, 2, 1])
    ])
    def test_play_check_who_win_treasure(
            self, players_gold_win, treasure, plays):
        handA, handB, handC, handD = \
            self._play_cards_against_room(treasure, plays)
        self.assertEqual(players_gold_win, [
            handA.player.gold,
            handB.player.gold,
            handC.player.gold,
            handD.player.gold])
