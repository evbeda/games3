import unittest
from . import GO, WINNING_PLAY
from unittest.mock import patch
from parameterized import parameterized
from .diez_mil import DiezMil
from .play import Play
from .turn import Turn
from .player import Player
from .exceptions.exceptions import PlayRemainsWithNoScore
from . import (
    PLAYER_CHOOSING_DICE_MESSAGE,
    PLAYERS_NAME_MESSAGE,
    NEXT_PLAYER_TURN_MESSAGE,
    PLAYERS_SET,
    CANT_SAVE_THOSE_DICES,
)


class TestDiezMil(unittest.TestCase):
    def setUp(self):
        self.game = DiezMil()
        self.play = Play()
        self.game.players_qty = 2
        self.game.base_score = 450

    def test_check_players_qty(self):
        self.assertEqual(self.game.check_players_qty(0), False)

    @parameterized.expand([
        (1, 3, 2,),
        (1, 5, 2,),
        (2, 5, 3,),
        (3, 5, 4,),
        (4, 5, 5,),
        (5, 5, 1,),
    ])
    def test_next_player(self, who_is_playing, players_qty, expected):
        self.game.who_is_playing = who_is_playing
        self.game.players_qty = players_qty
        self.game.players = [Player(str(i)) for i in range(players_qty)]
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
        ([4, 1, 1, 1, 1], ([1, 1, 1, 1], 2000)),  # four_ones
        ([5, 5, 5, 5, 5], ([5, 5, 5, 5, 5], 2000)),  # five_fives
    ])
    def test_calculate_repeated(self, dices, expected_score):
        self.assertEqual(self.play.calculate_repeated(dices), expected_score)

    @parameterized.expand([
        ([1, 1, 1, 4, 5], 1050),
        ([1, 1, 1, 1, 5], 2050),
        ([1, 1, 1, 1, 1], WINNING_PLAY),
        ([1, 4, 3, 4, 5], 150),
        ([3, 3, 3, 4, 5], 350),
        ([1, 2, 3, 4, 5], 500),
        ([2, 3, 4, 5, 6], 500),
        ([4, 4, 4, 4, 5], 850),
    ])
    def test_check_combination(self, dices, expected_result):
        self.assertEqual(self.play.check_combination(dices), expected_result)

    def test_first_play_of_the_turn_five_dices_number_of_dices(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        turn._generate_play()
        self.assertEqual(len(turn.plays[-1].dices), 5)

    def test_after_plays_of_the_same_turn_number_of_dices(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        with patch('random.randint', side_effect=[1, 1, 1, 1, 1]):
            turn._generate_play()
        turn.plays[-1].select_dices([0, 1])
        self.assertEqual(len(turn.plays[-1].dices), 2)

    def test_play_select_dice(self):
        play = Play()
        play.dices = [1, 5, 6, 4, 2]
        dices_selected = play.choose_dices([1, 2])
        self.assertEqual(dices_selected, [5, 6])

    def test_create_players(self):
        PLAYER1_NAME = 'PLAYER1_NAME'
        PLAYER2_NAME = 'PLAYER2_NAME'
        player_names = [PLAYER1_NAME, PLAYER2_NAME]
        self.game.create_players(player_names)
        self.assertEqual(
            [x.name for x in self.game.players],
            player_names
        )

    # to do parameterize with different plays
    def test_calculate_acumulated_score(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        turn.plays = []
        previous_score = player.actual_score
        turn.calculate_acumulated_score()
        new_score = player.actual_score
        self.assertEqual(previous_score - new_score, 0)

    def test_five_ones_win(self):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        with patch('random.randint', side_effect=[1, 1, 1, 1, 1]):
            turn._generate_play()
        turn.calculate_acumulated_score()
        self.assertEqual(turn.player.actual_score, 10000)

    def test_diezmil_next_turn_in_first_turn(self):
        game = DiezMil()
        self.assertEqual(game.next_turn(), PLAYERS_NAME_MESSAGE)

    def test_diezmil_next_turn_state_go(self):
        self.game.players = [Player('a'), Player('b')]
        self.game.state = GO
        self.game.actual_turn = Turn(self.game.players[0])
        self.game.actual_turn.plays[-1].is_playing = False
        self.assertEqual(self.game.next_turn(), NEXT_PLAYER_TURN_MESSAGE)

    @parameterized.expand([
        (True, PLAYER_CHOOSING_DICE_MESSAGE),
        (False, NEXT_PLAYER_TURN_MESSAGE),
    ])
    def test_diezmil_next_turn_state_go_playing(self, state, message):
        self.game.players = [Player('a'), Player('b')]
        self.game.state = GO
        self.game.actual_turn = Turn(self.game.players[0])
        self.game.actual_turn.plays.append(self.play)
        self.game.actual_turn.plays[-1].is_playing = state
        self.assertEqual(self.game.next_turn(), message)

    @parameterized.expand([
        ('Juan, Julian', ),
        ('Facundo, Nahuel', ),
        ('Nicolas,Gabriel', ),
        ('Martin,Walter', ),
    ])
    def test_diezmil_play_with_valid_input_for_names(self, input):
        names = input.split(',')
        self.assertEqual(self.game.play(input), PLAYERS_SET)
        for i in range(2):
            self.assertEqual(self.game.players[i].name, names[i])

    def test_parse_input(self):
        self.assertEqual(DiezMil.parse_input("1,3,4"), [1, 3, 4])

    @parameterized.expand([
        ([1, 2, 3, 4, 5], [1, 2, 3]),
        ([3, 3, 3], [0, 2]),
        ([1, 2, 2, 3, 3], [(1, 2, 3, 4)]),
        ([1, 1, 1, 1, 2], [4]),
    ])
    def test_play_cant_keep_dices_with_no_score(self, dices, keep):
        self.play.dices = dices
        with self.assertRaises(PlayRemainsWithNoScore):
            self.play.select_dices(keep)

    @parameterized.expand([
        ([1],),
        ([2],),
        ([3],),
        ([1, 2],),
        ([1, 3],),
        ([2, 3],),
    ])
    def test_turn_cant_keep_dices_with_no_score(self, keep):
        player = Player('TEST_PLAYER')
        turn = Turn(player)
        with patch('random.randint', side_effect=[1, 2, 2, 2, 5]):
            turn._generate_play()
        with self.assertRaises(PlayRemainsWithNoScore):
            turn.select_dices(keep)

    @parameterized.expand([
        ("1",),
        ("2",),
        ("3",),
        ("1,2",),
        ("1,3",),
        ("2,3",),
    ])
    def test_game_cant_keep_dices_with_no_score(self, user_input):
        with patch('random.randint', side_effect=[1, 2, 2, 2, 5]):
            self.game.play("a")
        returned = self.game.play(user_input)
        self.assertEqual(returned, CANT_SAVE_THOSE_DICES)

    def test_generate_play_if_score_cero(self):
        class ControlRandomValues(object):
            def __init__(self, *args, **kwargs):
                self.values = [2, 2, 3, 3, 4]
                self.play_count = -1

            def __call__(self, *args):
                self.play_count += 1
                if self.play_count > 4:
                    self.play_count = 0
                return self.values[self.play_count]

        with patch(
            'diezmil.play.random.randint',
                side_effect=ControlRandomValues()):

            turn = Turn(Player('A'))
            turn._generate_play(5)
            self.assertEqual(turn.is_playing(), False)

    # Show Tests

    @parameterized.expand([
        (5, [1, 2, 3, 3, 4], "Dices: [1, 2, 3, 3, 4]\n"
                             "Play score 100\n"),
        (5, [1, 2, 3, 4, 5], "Dices: [1, 2, 3, 4, 5]\n"
                             "Play score 500\n"),
        (2, [1, 1], "Dices: [1, 1]\n"
                    "Play score 200\n"),
    ])
    def test_play_str(self, dices_qty, dices_outcome, expected):
        with patch('random.randint', side_effect=dices_outcome):
            self.play.roll_dices(dices_qty)
        self.assertEqual(str(self.play), expected)

    def test_turn_str(self):
        player = Player('TEST_PLAYER')
        with patch('random.randint', side_effect=[1, 2, 3, 3, 5]):
            turn = Turn(player)
        with patch('random.randint', side_effect=[4, 4, 4]):
            turn.select_dices([0, 4])

        expected = 'Player: TEST_PLAYER\n'
        expected += 'Score: 0\n'
        expected += '====================\n'
        expected += 'Play:\n'
        expected += 'Dices: [1, 5]\n'
        expected += 'Play score 150\n'
        expected += '====================\n'
        expected += 'Play:\n'
        expected += 'Dices: [4, 4, 4]\n'
        expected += 'Play score 400\n'

        self.assertEqual(turn.build_board(), expected)

    def test_diez_mil_board_empty(self):
        self.assertEqual(self.game.board, '')

    def test_diez_mil_board_not_empty(self):
        with patch('random.randint', side_effect=[1, 2, 3, 3, 5]):
            self.game.play('TEST_PLAYER')
        with patch('random.randint', side_effect=[4, 4, 4]):
            self.game.play('0,4')

        expected = 'Player: TEST_PLAYER\n'
        expected += 'Score: 0\n'
        expected += '====================\n'
        expected += 'Play:\n'
        expected += 'Dices: [1, 5]\n'
        expected += 'Play score 150\n'
        expected += '====================\n'
        expected += 'Play:\n'
        expected += 'Dices: [4, 4, 4]\n'
        expected += 'Play score 400\n'

        self.assertEqual(self.game.board, expected)
