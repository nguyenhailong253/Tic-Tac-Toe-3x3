# author: long nguyen (nguyenhailong253@gmail.com)

# +  -  -  - CONSTANTS -  -  - +
NUM_ROWS = 3
NUM_COLUMNS = 3
DOT = "."


class Board(object):
    ''' 3x3 Board for TicTacToe game '''

    def __init__(self):
        # list of 3 lists with 3 elements (3x3)
        self.board = [[DOT for x in range(NUM_ROWS)]
                      for y in range(NUM_COLUMNS)]

        # counter for coordinates filled
        self.coordinates_filled = 0

    def get_board(self):
        return self.board

    def draw_board(self):
        ''' Draw 3x3 board  '''

        print("\n")
        for x in range(NUM_ROWS):
            for y in range(NUM_COLUMNS):
                print(self.board[x][y], end=' ')
            print("\n")

    def insert_move(self, x, y, player_symbol):
        ''' Insert player symbol to corresponding coordinates '''
        self.board[x][y] = player_symbol

        if not self.is_board_filled():
            self.coordinates_filled += 1

    # +  -  -  - CONDITIONS FOR WIN/DRAW -  -  - +

    def is_row_filled(self):
        ''' Check if any of the 3 rows is filled with 1 symbol '''

        for row in self.board:
            if row[0] == row[1] == row[2] != DOT:
                return True
        return False

    def is_column_filled(self):
        ''' Check if any of the 3 columns is filled with 1 symbol '''

        for column in range(NUM_COLUMNS):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != DOT:
                return True
        return False

    def is_diagonal_filled(self):
        ''' Check if any of the 2 diagonals is filled with 1 symbol '''

        # left to rigght diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        # right to left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False

    def is_board_filled(self):
        ''' Check if the whole board is filled '''
        return self.coordinates_filled == NUM_COLUMNS * NUM_ROWS
