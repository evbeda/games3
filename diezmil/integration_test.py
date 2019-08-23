from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
from .diez_mil import DiezMil
from .turn import Turn
from .play import Play
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
        # self.game.actual_turn = Turn(1)

    @parameterized.expand([
        (SETUP, 'Please, input comma separated names'),
        (GO, 'Choose dice'),
        (GO, 'Next player turn'),
    ])
    def test_next_turn(self, state, message):
        self.game.state = state
        self.assertEqual(message, self.game.next_turn())

    @parameterized.expand([
        ('STAY'),
        ('0,1'),
        (GO, 'Next player turn'),
    ])
    def test_play_stay(self):
        self.game.next_player()




    # def test_show_board(self):
    #     play_one = Play()
    #     play_one.play_score = 600
    #     play_one.dices = [6, 6, 6, 2, 3]
    #     play_one.is_playing = False
    #     play_two = Play()
    #     play_two.play_score = 1000
    #     play_two.is_playing = False
    #     play_two.dices = [1, 1, 1, 1, 3]
    #     self.assertEqual(
    #         "Player: TEST_PLAYER\n" +\
    #         "Score: 0\n" +\
    #         "====================\n" +\
    #         "Play:\n" +\
    #         "Dices: [6, 6, 6, 2, 3]\n" +\
    #         "Play score 600\n" +\
    #         "====================\n" +\
    #         "Play:\n" +\
    #         "Dices: [1, 1, 1, 1, 3]\n" +\
    #         "Play score 1000\n", self.game.board)
    # def test_resolve_command_method(self):
    #     result = self.game.resolve_command('STRAIGHT_BET 14 100')
        # self.assertEqual(('STRAIGHT_BET', [14], 100), result)

    # @parameterized.expand([
    #     (END_GAME_COMMAND, '', '', BYE_MESSAGE),
    #     ('STRAIGHT_BET', '10', 15, SUCCESS_MESSAGE),
    #     ('STREET_BET', '1_2_3', 10, SUCCESS_MESSAGE),
    #     ('STRAIGHT_BET', '40', 10, INVALID_BET_MESSAGE),
    #     ('INVALID_BET', '10', 15, INVALID_BET_TYPE_MESSAGE),
    #     ('STRAIGHT_BET', '20', 200, NOT_ENOUGH_CASH_MESSAGE)
    # ])
    # def test_user_typing_return_message(
    #         self, bet_type, bet_value, amount, expected_message):
    #     self.assertEqual(expected_message, self.game.play(
    #         bet_type, bet_value, amount))

    # @patch('ruleta.roulette.randint', return_value=30)
    # def test_play_round_win(self, mock_randint):
    #     self.player = Player(50)
    #     self.game.croupier.add_bet(StraightBet([30], 25))
    #     self.assertEqual(
    #         WON_MESSAGE + '875 chips\nRANDOM NUMBER: 30',
    #         self.game.play(GO_COMMAND)
    #         )

    # @patch('ruleta.roulette.randint', return_value=31)
    # def test_play_round_lost(self, mock_randint):
    #     self.player = Player(50)
    #     self.game.croupier.add_bet(StraightBet([30], 25))
    #     self.assertEqual(
    #         LOST_MESSAGE + '\nRANDOM NUMBER: 31', self.game.play(GO_COMMAND))


