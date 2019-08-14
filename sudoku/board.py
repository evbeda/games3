class Board():
    def __init__(self, board):
        self.board = self.build_board(board)

    def build_board(self, board):
        return {
            'a':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[0:9]],
            'b':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[9:18]],
            'c':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[18:27]],
            'd':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[27:36]],
            'e':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[36:45]],
            'f':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[45:54]],
            'g':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[54:63]],
            'h':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[63:72]],
            'i':
            [{'val':i, 'mod':True} if i == ' ' else {'val':i, 'mod':False} for i in board[72:81]]
        }

    def is_modifiable(self, row, column):
        board_row = self.board[row.lower()]
        board_colum = int(column-1)
        return board_row[board_colum]['mod']

    def place(self, coordinates, value):
        value = str(value)
        row, column = coordinates
        self.board[row][column - 1]['val'] = value
