import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..model import EXIT
from ..model.exceptions.exceptions import (
    NotCorrectSelectedCardException,
    NotANumberException,
)
from ..model.player import ComputerPlayer, HumanPlayer
from ..model.game import Game


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
        game.play(EXIT)
        self.assertFalse(game.is_playing)

    def test_game_levels(self):
        game = Game()
        self.assertEqual(game.current_level, game.levels[0])

