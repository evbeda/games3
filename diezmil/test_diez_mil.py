import unittest
from . import SETUP, GO, WINNING_PLAY
from unittest.mock import patch
from parameterized import parameterized
from .diez_mil import DiezMil
from .play import Play
from .turn import Turn
from .player import Player
from .exceptions.exceptions import NegativePlayersQuantityException, \
    NullPlayersQuantityException, DifferentPlayerQuantityAndNamesException, \
    ManyPlayersQuantityException, NotCorrectPlayersQuantityException, \
    NotANumberException


class TestDiezMil(unittest.TestCase):
    def setUp(self):
        self.game = DiezMil()
        self.play = Play()
        self.game.players_qty = 2
        self.game.baseScore = 450

    def test_check_players_qty(self):
        self.assertEqual(self.game.check_players_qty(0), False)

    @parameterized.expand([
        (1, ['Lenny'], [Player('Lenny')]),
        (2, ['Lenny', 'Carl'], [Player('Lenny'), Player('Carl')]),
    ])
    def test_players_creator(self, players_quantity, names, expected_players):
        players = self.game.players_creator(players_quantity, names)
        for player in players:
            index = players.index(player)
            self.assertTrue(player.__gt__(expected_players[index]))

    @parameterized.expand([
        (-1, [], NegativePlayersQuantityException),
        (0, [], NullPlayersQuantityException),
        (2, ['Lenny'], DifferentPlayerQuantityAndNamesException),
        (1, ['Lenny', 'Carl'], DifferentPlayerQuantityAndNamesException),
        (6, [], ManyPlayersQuantityException),
    ])
    def test_players_creator_exceptions(self, players_quantity, names, exc):
        with self.assertRaises(exc):
            self.game.players_creator(players_quantity, names)

    @parameterized.expand([
        ('-1', NotCorrectPlayersQuantityException),
        ('0', NotCorrectPlayersQuantityException),
        ('%', NotANumberException),
        (' ', NotANumberException),
        ('_', NotANumberException),
    ])
    def test_ask_for_players_quantity_exceptions(self, players_quantity, exc):
        with patch('builtins.input', return_value=players_quantity):
            with self.assertRaises(exc):
                self.game.ask_for_players_quantity()

    @parameterized.expand([
        (1, 3, 1, SETUP),
        (1, 5, 2, GO),
        (2, 5, 3, GO),
        (3, 5, 4, GO),
        (4, 5, 5, GO),
        (5, 5, 1, GO),
    ])
    def test_next_player(self, who_is_playing, players_qty, expected, state):
        self.game.players_qty = players_qty
        self.game.state = state
        self.game.who_is_playing = who_is_playing
        self.game.next_player()
        self.assertEqual(expected, self.game.who_is_playing)

    # Play testings
    def test_roll_dices_error(self):
        self.assertEqual(self.play.roll_dices(7), False)

    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_5_dices(self, mock_randint):
        self.play.roll_dices(5)
        self.assertEqual(self.play.dices, [1, 1, 1, 1, 1])

    @patch('diezmil.play.random.randint', return_value=1)
    def test_roll_3_dices(self, mock_randint):
        self.play.roll_dices(3)
        self.assertEqual(self.play.dices, [1, 1, 1])

    @parameterized.expand([
        ([1, 5, 5], ([1, 5, 5], 200)),
        ([1, 5], ([1, 5], 150)),
        ([1, 5, 1, 2, 3], ([1, 1, 5], 250)),
        ([2, 3, 2], ([], 0)),
        ([5], ([5], 50)),
    ])
    def test_individual_values(self, dices, expected_score):
        score = self.play.calculate_individual_values(dices)
        self.assertEqual(score, expected_score)

    # Test is a stair
    @parameterized.expand([
        ([1, 2, 3, 4, 5], True),
        ([1, 3, 2, 5, 4], True),
        ([2, 3, 4, 5, 6], True),
        ([3, 2, 5, 4, 6], True),
        ([1, 1, 3, 4, 2], False),
        ([1, 1, 5, 4, 4], False),
    ])
    def test_is_a_stair(self, dices, expected):
        self.assertEqual(self.play.is_a_stair(dices), expected)

    # Test is a repeated
    @parameterized.expand([
        ([1, 1, 1, 3, 2], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 1, 1], True),
    ])
    def test_is_repeated(self, dices, expected):
        self.assertEqual(self.play.is_repeated(dices), expected)

    # Test calculate repeated
    @parameterized.expand([
        ([2, 3, 3, 4, 4], ([], 0)),  # no score
        ([1, 3, 3, 3, 3], ([3, 3, 3, 3], 600)),  # quadruple
        ([4, 1, 1, 1, 1], ([1, 1, 1, 1], 2000)),  # four_ones
        ([5, 5, 5, 5, 5], ([5, 5, 5, 5, 5], 2000)),  # five_fives
    ])
    def test_calculate_repeated(self, dices, expected_score):
        self.assertEqual(self.play.calculate_repeated(dices), expected_score)

    @parameterized.expand([
        ([1, 1, 1, 4, 5], ([1, 1, 1], 1000)),
        ([1, 1, 1, 1, 5], ([1, 1, 1, 1], 2000)),
        ([1, 1, 1, 1, 1], ([1, 1, 1, 1, 1], WINNING_PLAY)),
        ([1, 4, 3, 4, 5], ([1, 5], 150)),
        ([3, 3, 3, 4, 5], ([3, 3, 3], 300)),
        ([1, 2, 3, 4, 5], ([1, 2, 3, 4, 5], 500)),
        ([2, 3, 4, 5, 6], ([2, 3, 4, 5, 6], 500)),
        ([4, 4, 4, 4, 5], ([4, 4, 4, 4], 800)),
    ])
    def test_check_combination(self, dices, expected_result):
        self.assertEqual(self.play.check_combination(dices), expected_result)

    def test_first_play_of_the_turn_five_dices_number_of_dices(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        turn.generate_play()
        self.assertEqual(len(turn.plays[-1].dices), 5)

    def test_after_plays_of_the_same_turn_number_of_dices(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        turn.generate_play()
        turn.plays[-1].select_dices([0, 1])
        turn.generate_play()
        self.assertEqual(len(turn.plays[-1].dices), 3)

    def test_play_select_dice(self):
        play = Play()
        play.dices = [1, 5, 6, 4, 2]
        dices_selected = play.choose_dices([1, 2])
        self.assertEqual(dices_selected, [5, 6])

    def test_create_players(self):
        PLAYER1_NAME = 'PLAYER1_NAME'
        PLAYER2_NAME = 'PLAYER2_NAME'
        player_names = [PLAYER1_NAME, PLAYER2_NAME]
        with patch('builtins.input', side_effect=player_names):
            self.game.create_players()
        self.assertEqual(
            [x.name for x in self.game.players],
            player_names
        )

    def test_calculate_acumulated_score(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        turn.plays = []
        turn.calculate_acumulated_score()
        self.assertEqual(turn.acumulated_score, 0)

    def test_five_ones_win(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        with patch('random.randint', side_effect=[1, 1, 1, 1, 1]):
            turn.generate_play()
        turn.calculate_acumulated_score()
        self.assertEqual(turn.player.actual_score, 10000)


    # USAR PARA EL TEST - NO BORRAR
    # @parameterized.expand([
    #     ('SELECT_DICES 1 3'),
    #     ('PLAY_AGAIN'),
    #     ('NO_MORE_GAMING')
    # ])
    # def test_play(self, state):
    #     self.game.state = state
    #     self.game.play()


if __name__ == '__main__':
    unittest.main()
