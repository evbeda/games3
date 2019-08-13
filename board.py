class Board():
    def __init__(self, board):
        self.board = self.build_board(board)
        
        
    def build_board(self, board):
        return {
            'a': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[0:9]],
            'b': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[9:18]],
            'c': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[18:27]],
            'd': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[27:36]],
            'e': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[36:45]],
            'f': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[45:54]],
            'g': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[54:63]],
            'h': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[63:72]],
            'i': [{'valor': i,'modifiable': True} if i == ' ' else {'valor': i,'modifiable': False} for i in board[72:81]]
        }
    
    def unchangeable(self, row, column):
        board_row = self.board[row.lower()]
        board_colum = int(column-1)
        return board_row[board_colum]['modifiable']