import unittest
from ..model.exceptions.exceptions import UnplayableCardException
from ..model.hand_player import HandPlayer
from ..model.game import Game
from ..model.player import Player


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

