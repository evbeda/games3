from .board import Board


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

    # TODO use API
    # def get_board(self):
    #     pass

    def next_turn(self):
        if self.is_playing:
            return "Place a number"
        else:
            return "Game over"

    # user_input = "a 1 4"
    def play(self, user_input):
        row, column, value = user_input.split(" ")
        try:
            place = self.game_board.place((row, int(column)), int(value))
        except Exception:
            return 'You can not modify the initial values.'
        if self.game_board.is_finished():
            self.is_playing = False
            return 'You win!'
        return place

    # TODO print
    # @property
    # def board(self):
    #     pass
