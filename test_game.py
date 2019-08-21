import unittest
from unittest.mock import patch

from sudoku import (
    ALMOST_FINISHED_EXAMPLE_BOARD,
    ALMOST_FINISHED_SHOWN_BOARD,
    FINISHED_SHOWN_BOARD,
    YOU_WIN
    )
from uno.const import (
    UNO_FINAL_LAST_PLAYED_CARD,
    UNO_FINAL_PLAYER_CARD,
    UNO_ALMOST_FINISHED_BOARD,
    UNO_FINISHED_BOARD,
    )
from craps.constants import (
    CRAPS_FIRST_BOARD,
    CRAPS_YOU_WON,
    BET_PLACED_SUCCESFULLY,
    CRAPS_BET_PLACED,
)
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        class OutputCollector(object):
            def __init__(self, *args, **kwargs):
                self.output_collector = []

            def __call__(self, output):
                self.output_collector.append(output)

        self.output_collector = OutputCollector()

    @patch('game.Game.get_input', return_value='9')
    def test_quit_game(self, mock_input):
        with patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            [],
        )

    def test_game_selection(self):
        self.assertEqual(
            self.game.game_inputs(),
            'Select Game\n'
            '0: Guess Number Game\n'
            '1: Sudoku Game\n'
            '2: Roulette\n'
            '3: Uno Game\n'
            '4: Diezmil Game\n'
            '5: Craps Game\n'
            '6: Dungeon Raiders\n'
            '9: to quit\n'
        )

    def test_play_guess_number_game(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '0'
                if 'Give me a number from 0 to 100' in console_output:
                    return '50'

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()), \
                patch(
                    'game.Game.output', side_effect=self.output_collector), \
                patch(
                    'guess_number_game.guess_number_game.randint',
                    return_value=50):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            ['[]', 'you win', '[50]'],
        )

    def test_play_sudoku(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = -1
                self.plays = [
                    'a 1 2',
                ]

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '1'
                self.play_count += 1
                return self.plays[self.play_count]

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()
                    ), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch(
                    'sudoku.game.fetch_board',
                    return_value=ALMOST_FINISHED_EXAMPLE_BOARD,
                ):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            [ALMOST_FINISHED_SHOWN_BOARD, YOU_WIN, FINISHED_SHOWN_BOARD],
         )

    def test_play_roulette(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = -1
                self.plays = [
                    'COLOR_BET RED 40',
                    'GO GO GO',
                    'END_GAME END_GAME END_GAME'
                ]

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '2'
                self.play_count += 1
                return self.plays[self.play_count]

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()
                    ), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch(
                    'sudoku.game.fetch_board',
                    return_value=ALMOST_FINISHED_EXAMPLE_BOARD,
                ):
            self.game.play()

        # expected output history
        # self.assertEqual(
        #    self.output_collector.output_collector,
        #    [],
        # )

    # def test_play_uno(self):

    #     class ControlInputValues(object):
    #         def __init__(self, *args, **kwargs):
    #             self.played = False
    #             self.play_count = 0
    #             self.plays = [
    #                 '1',
    #             ]

    #         def __call__(self, console_output):
    #             if 'Select Game' in console_output:
    #                 if self.played:
    #                     return '9'
    #                 self.played = True
    #                 return '3'
    #             # self.play_count += 1
    #             return self.plays[self.play_count]

    #     with \
    #             patch(
    #                 'game.Game.get_input', side_effect=ControlInputValues()
    #                 ), \
    #             patch('game.Game.output', side_effect=self.output_collector), \
    #             patch(
    #                 'uno.stack.Stack.generate_cards',
    #                 return_value=[UNO_FINAL_LAST_PLAYED_CARD]
    #             ), \
    #             patch(
    #                 'uno.stack.Stack.generate_cards_player',
    #                 return_value=[UNO_FINAL_PLAYER_CARD]
    #             ):
    #         self.game.play()
    #     self.assertEqual(
    #         self.output_collector.output_collector,
    #         [UNO_ALMOST_FINISHED_BOARD, "You WON", UNO_FINISHED_BOARD],
    #      )

    def test_play_craps(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = -1
                self.plays = [
                    'PASS_BET 200',
                    'GO',
                    'NO'
                ]

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '5'
                self.play_count += 1
                return self.plays[self.play_count]

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()
                    ), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch(
                    'random.sample',
                    return_value=[3, 4],
                ):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            [
                CRAPS_FIRST_BOARD,
                BET_PLACED_SUCCESFULLY,
                CRAPS_BET_PLACED,
                (3, 4),
                CRAPS_YOU_WON,
                'Game Over',
                CRAPS_YOU_WON,
                   ],
         )


if __name__ == "__main__":
    unittest.main()
