import unittest
from unittest.mock import patch
from parameterized import parameterized
from .model.player import Player, ComputerPlayer, HumanPlayer
from .model.hand_player import HandPlayer
from .model.game import Game
from .model.level import Level
from .model.rooms.monster_room import MonsterRoom
from .model.rooms.gold_room import GoldRoom
from .model.rooms.wound_room import WoundRoom
from .model.rooms.treasure import Treasure
from .model.exceptions.exceptions import UnplayableCardException, \
    NotANumberException, NotCorrectSelectedCardException
from .model import GOLDS, WOUNDS, EXIT


class TestDungeon(unittest.TestCase):

    """ -------------------- Player tests -------------------- """
    def test_init_hand(self):
        hand = HandPlayer(Player('A'))
        self.assertEqual(5, len(hand.cards_to_play))

    def test_check_if_player_can_play_card_2(self):
        hand = HandPlayer(Player('A'))
        hand.play(2)
        hand.play(5)
        with self.assertRaises(UnplayableCardException):
            hand.play(2)

    def test_check_actual_card(self):
        hand = HandPlayer(Player('A'))
        hand.play(2)
        self.assertEqual(2, hand.last_card_played)

    def test_check_if_3_is_in_hand(self):
        hand = HandPlayer(Player('A'))
        hand.play(3)
        self.assertTrue(3 not in hand.cards_to_play)

    """ -------------------- Game tests -------------------- """
    def test_check_if_game_has_5_levels(self):
        game = Game()
        self.assertEqual(5, len(game.levels))

    def test_check_if_player_a_wins(self):
        game = Game()
        game.players[0].gold = 50
        game.players[0].wounds = 10
        game.players[1].gold = 40
        game.players[1].wounds = 15
        game.players[2].gold = 60
        game.players[2].wounds = 20    
        self.assertEqual(game.players[0], game.get_winner())

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
        handA, handB, handC, handD = \
            self._play_cards_against_room(treasure, plays)
        self.assertEqual(players_gold_win, [
            handA.player.gold,
            handB.player.gold,
            handC.player.gold,
            handD.player.gold])


class TestLevel(unittest.TestCase):
    def test_check_if_each_levels_has_five_rooms(self):
        level = Level([Player('A'), Player('B'), Player('C')])
        self.assertEqual(5, len(level.rooms))


class TestPlayer(unittest.TestCase):
    @parameterized.expand([
        (ComputerPlayer(), [3, 4, 5]),
        (ComputerPlayer(), [1, 2, 3, 4, 5]),
        (ComputerPlayer(), []),
    ])
    def test_select_card_computer_player_valid(self, player, cards):
        selected_card = player.select_card(cards)
        self.assertTrue(True, selected_card in cards)

    @parameterized.expand([
        ([1, 2, 3, 4, 5], '1'),
        ([1, 2, 3, 4, 5], '5'),
        ([1, 2, 3], '3'),
    ])
    def test_select_card_human_player_valid(self, cards, sel_card):
        with patch('builtins.input', return_value=sel_card):
            self.assertTrue(HumanPlayer().select_card(cards))

    @parameterized.expand([
        ([1, 2, 3, 4], '5', NotCorrectSelectedCardException),
        ([1, 2, 3, 4], '0', NotCorrectSelectedCardException),
        ([1, 2, 3, 4, 5], '%', NotANumberException),
        ([1, 2, 3, 4, 5], '_', NotANumberException),
    ])
    def test_select_card_human_player_not_valid(self, cards, sel_card, exc):
        with self.assertRaises(exc):
            with patch('builtins.input', return_value=sel_card):
                self.assertTrue(HumanPlayer().select_card(cards))

    def test_game_is_playing(self):
        game = Game()
        self.assertTrue(game.is_playing)
        game.play(command=EXIT)
        self.assertFalse(game.is_playing)

    def test_game_levels(self):
        game = Game()
        self.assertEqual(game.current_level, game.levels[0])

