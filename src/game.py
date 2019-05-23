# author: long nguyen (nguyenhailong253@gmail.com)

from src.board import Board
from src.messages import Messages

PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_1_SYMBOL = 'X'
PLAYER_2_SYMBOL = 'O'


class Game(object):
    ''' Game engine for TicTacToe '''

    def __init__(self):
        self.current_player = PLAYER_1
        self.current_symbol = PLAYER_1_SYMBOL

        # user input x,y coordinates
        self.input_coordinates = []

        # game over flag
        self.game_over = False

    def validate_input(self):
        pass

    def display_win_message(self):
        pass

    def display_draw_message(self):
        pass

    def run_game(self):
        pass
