import unittest
from unittest.mock import patch
from parameterized import parameterized
from .game import CrapsGame
from .turn import Turn
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_STARTED,
    GAME_IN_PROGRESS,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
)


class TestCraps(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_craps_game_started(self):
        self.assertTrue(self.game.is_playing)
        self.assertIsInstance(self.game.turn, Turn)

    def test_craps_game_started_asks_for_a_bet(self):
        self.assertEqual(self.game.turn.state, GAME_STARTED)
        self.assertEqual(self.game.next_turn(), BET_MESSAGE)

    def test_craps_game_in_progress_asks_for_a_bet(self):
        self.game.turn.state = GAME_IN_PROGRESS
        self.assertEqual(self.game.next_turn(), BET_MESSAGE)

    def test_craps_player_lost_aks_keep_playing(self):
        self.game.turn.state = PLAYER_LOST
        self.assertEqual(self.game.next_turn(), LOST_MESSAGE)

    def test_craps_player_won_aks_keep_playing(self):
        self.game.turn.state = PLAYER_WON
        self.assertEqual(self.game.next_turn(), WON_MESSAGE)

    def test_craps_player_wants_to_quit(self):
        self.assertEqual(self.game.play('No'), 'Game Over')

    @parameterized.expand([
        ((2, 2),),
        ((2, 3),),
        ((4, 2),),
        ((4, 4),),
        ((5, 4),),
        ((5, 5),),
    ])
    def test_craps_play_returns_score(self, dice):
        with patch('random.sample', return_value=dice):
            self.assertEqual(self.game.play('Go'), dice)
