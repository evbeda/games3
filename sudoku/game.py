from . import NUMBER_ADDED, PLACE_A_NUMBER, GAME_OVER, YOU_WIN
from .board import Board
from .api import fetch_board


class SudokuGame:

    name = 'Sudoku Game'

    def __init__(self, board=None):
        if not board:
            board = fetch_board()
        self.game_board = Board(board)
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

    @property
    def board(self):
        ret = ""
        for k, row in self.game_board.board.items():
            for index, item in enumerate(row):
                ret += item["val"] + " "
                if index in [2, 5]:
                    ret += "|"
            ret += "\n"
            if k in ['c', 'f']:
                ret += "------+------+------\n"
        return ret
