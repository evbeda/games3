from .board import Board
from . import NUMBER_ADDED, PLACE_A_NUMBER, GAME_OVER, YOU_WIN


class SudokuGame:

    name = 'Sudoku Game'

    def __init__(self):
        # Hardcoded for tests. Should use get_board api
        self.game_board = Board(
            " 6 3  8 4"
            "537 9    "
            " 4   63 7"
            " 9  51238"
            "         "
            "71362  4 "
            "3 64   1 "
            "    6 523"
            "1 2  9 8 "
        )
        self.is_playing = True

    def next_turn(self):
        if self.is_playing:
            return PLACE_A_NUMBER
        else:
            return GAME_OVER

    # user_input = "a 1 4"
    def play(self, user_input):
        row, column, value = user_input.split(" ")
        try:
            self.game_board.place((row, int(column)), int(value))
            if self.game_board.is_finished():
                self.is_playing = False
                return YOU_WIN
            return NUMBER_ADDED
        except Exception as e:
            return str(e)
    
    # TODO print
    # @property
    # def board(self):
    #     pass
