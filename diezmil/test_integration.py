from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
from .diez_mil import DiezMil
from .turn import Turn
from .play import Play
from .player import Player
from . import (
    SETUP,
    GO,
    PLAYER_CHOOSING_DICE_MESSAGE,
    PLAYER_DONE_MESSAGE,
    PLAYERS_NAME_MESSAGE,
    NEXT_PLAYER_TURN_MESSAGE,
    PLAYERS_SET,
    CANT_SAVE_THOSE_DICES,
    )


class IntegrationTest(TestCase):
    # Test for the game diez mil
    def setUp(self):
        self.game = DiezMil()
        self.game.players_qty = 1
        self.who_is_playing = 1
        self.game.actual_turn = Turn(1)

    @parameterized.expand([
        (SETUP, 'Please, input comma separated names'),
        (GO, 'Choose dice'),
        # (GO, 'Next player turn'),
    ])
    def test_next_turn(self, state, message):
        self.game.state = state
        self.assertEqual(message, self.game.next_turn())

<<<<<<< HEAD
    # @parameterized.expand([
    #     ('STAY'),
    #     ('0,1'),
    #     (GO, 'Next player turn'),
    # ])
    # def test_play_stay(self):
    #     self.game.next_player()
=======
    @parameterized.expand([
        ('STAY'),
        ('0,1'),
        (GO, 'Next player turn'),
    ])
    def test_play(self):
        pass

    def test_show_board(self):
        test_board = 'Player: Agustin\n'
        test_board += 'Score: 0\n'
        for play in self.plays:
            test_board += '====================\n'
            test_board += 'Play:\n'
            test_board += 'Dices: [1, 1, 3, 5, 5]\n'
            test_board += 'Play score 300'
        player = Player('Agustin')
        turn = Turn(player)
        play = Play()
        play.play_score = 300
        play.dices = [1, 1, 3, 5, 5]
        turn.plays.append(play)
>>>>>>> test_board

        self.assertEqual(test_board, turn.build_board)
