# Modules
import unittest
from unittest.mock import patch
from parameterized import parameterized
# Model
from ..model.exceptions.exceptions import UnplayableCardException
from ..model.hand_player import HandPlayer
from ..model.game import Game
from ..model.player import Player
from ..model.rooms.wound_room import WoundRoom
from ..model.rooms.treasure import Treasure
from ..model.rooms.gold_room import GoldRoom
from ..model.rooms.monster_room import MonsterRoom
# Messages
from . import BOARD_EXAMPLE
from . import BOARD_EXAMPLE_TWO_WINNERS
from . import BOARD_EXAMPLE_WINNER
from . import ROOMS_EXAMPLE
from . import NEXT_TURN_WOUNDROOM_EXAMPLE
from . import NEXT_TURN_TREASURE_EXAMPLE
from . import NEXT_TURN_GOLDROOM_EXAMPLE
from . import NEXT_TURN_MONSTERROOM_EXAMPLE
from . import PLAYERS_EXAMPLE
from . import PLAYERS_EXAMPLE_TWO_WINNERS


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
        self.assertEqual(5, len(game.create_levels()))

    def test_check_if_game_has_3_players(self):
        game = Game()
        self.assertEqual(3, len(game.create_players()))

    @parameterized.expand([
        ([50, 10], [40, 20], [60, 20], [1, 2], [0, 1, 2], [2]),
        ([60, 10], [40, 20], [60, 20], [1, 2], [0, 1, 2], [0]),
        ([60, 10], [40, 20], [60, 10], [1], [0, 2], [0, 2]),
        ([60, 10], [60, 10], [60, 10], [0, 1, 2], [0, 1, 2], [0, 1, 2]),
    ])
    def test_check_resolve_game(self, player1, player2, player3,
                                max_wound, finalists, winner):
        game = Game()
        game.players[0].gold = player1[0]
        game.players[0].wounds = player1[1]
        game.players[1].gold = player2[0]
        game.players[1].wounds = player2[1]
        game.players[2].gold = player3[0]
        game.players[2].wounds = player3[1]
        expected_max_wound = [player for player in game.players
                              if game.players.index(player) in max_wound]
        expected_finalists = [player for player in game.players
                              if game.players.index(player) in finalists]
        expected_winners = [player for player in game.players
                            if game.players.index(player) in winner]
        # players_with_max_wounds
        players_max_wound = game.get_players_with_max_wounds(game.players)
        self.assertEqual(players_max_wound, expected_max_wound)
        # finalists
        finalists = game.get_finalists()
        self.assertEqual(finalists, expected_finalists)
        # winner/winner
        winners = game.resolve_game()
        self.assertEqual(winners, expected_winners)

    @patch(
        'dungeon_raiders.model.level.Level.select_rooms',
        return_value=ROOMS_EXAMPLE
        )
    @patch(
        'dungeon_raiders.model.game.Game.create_players',
        return_value=PLAYERS_EXAMPLE
        )
    def test_board(self, mocked_rooms, mocked_players):
        game = Game()
        self.assertEqual(BOARD_EXAMPLE, game.board)

    @patch(
        'dungeon_raiders.model.game.Game.create_players',
        return_value=PLAYERS_EXAMPLE
        )
    def test_board_is_game_over(self, _):
        game = Game()
        game.is_playing = False
        self.assertEqual(BOARD_EXAMPLE_WINNER, game.board)

    @patch(
        'dungeon_raiders.model.game.Game.create_players',
        return_value=PLAYERS_EXAMPLE_TWO_WINNERS
        )
    def test_board_is_game_over_two_winners(self, _):
        game = Game()
        game.is_playing = False
        self.assertEqual(BOARD_EXAMPLE_TWO_WINNERS, game.board)

    def test_next_turn_monster_room(self):
        game = Game()
        game.current_level.actual_room = MonsterRoom((11, 3, 'Esqueleto'))
        self.assertEqual(NEXT_TURN_MONSTERROOM_EXAMPLE, game.next_turn())

    @parameterized.expand([
        (NEXT_TURN_MONSTERROOM_EXAMPLE, MonsterRoom((11, 3, 'Esqueleto'))),
        (NEXT_TURN_GOLDROOM_EXAMPLE, GoldRoom(
            ['Caldero de lava', [(5, 3), (4, 2), (3, 1)]])),
        (NEXT_TURN_WOUNDROOM_EXAMPLE, WoundRoom(
            ['Trampa de pinchos', [(5, 2), (4, 2), (3, 1)]])),
        (NEXT_TURN_TREASURE_EXAMPLE, Treasure((4, 2))),
        ])
    def test_next_turn_gold_room(self, example, room):
        game = Game()
        game.current_level.actual_room = room
        self.assertEqual(example, game.next_turn())
