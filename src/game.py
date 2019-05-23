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

    def is_input_numerical(self, x_input, y_input):
        ''' Check if x,y are numerical '''

        if isinstance(x_input, int) and isinstance(y_input, int):
            return True
        return False

    def is_input_within_range(self, x_input, y_input):
        ''' Check if x,y are within range 1 to 3 '''

        valid_range = range(1, 4)  # from 1 to 3
        if x_input in valid_range and y_input in valid_range:
            return True
        return False

    def validate_input(self):
        ''' Validate if input is numerical and within range '''

        if len(self.input_coordinates) == 2:
            # deconstruct list of inputs
            x_input = self.input_coordinates[0]
            y_input = self.input_coordinates[1]

            if self.is_input_numerical(x_input, y_input):
                if self.is_input_within_range(x_input, y_input):
                    return True
                else:
                    # display out of range message
                    pass
            else:
                # display not numerical message
                pass
        else:
            # display too many/few inputs
            pass
        return False

    def display_win_message(self):
        pass

    def display_draw_message(self):
        pass

    def run_game(self):
        pass