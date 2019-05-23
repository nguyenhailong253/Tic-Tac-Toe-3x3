# author: long nguyen (nguyenhailong253@gmail.com)

from src.board import Board
from src.messages import MESSAGES

PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_1_SYMBOL = 'X'
PLAYER_2_SYMBOL = 'O'


class Game(object):
    ''' Game engine for TicTacToe '''

    def __init__(self):
        # first player is always X
        self.current_player = PLAYER_1
        self.current_symbol = PLAYER_1_SYMBOL

        self.board = Board()

        # user input x,y coordinates
        self.input_coordinates = []
        self.x_input = None
        self.y_input = None

        # game over flag
        self.game_over = False

    # +  -  -  - INPUT VALIDATION -  -  - +

    def is_input_numerical(self, x_input, y_input):
        ''' Check if x,y are numerical '''
        try:
            if isinstance(int(x_input), int) and isinstance(int(y_input), int):
                return True
        except:
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
                x_input = int(x_input)
                y_input = int(y_input)
                if self.is_input_within_range(x_input, y_input):
                    # display valid input message
                    print(MESSAGES['valid_input'])
                    self.x_input = x_input - 1
                    self.y_input = y_input - 1
                    return True
                else:
                    # display out of range message
                    print(MESSAGES['out_of_range'])
            else:
                # display non-numerical message
                print(MESSAGES['wrong_type'])
        else:
            # display too many/few inputs
            print(MESSAGES['wrong_num_inputs'])

        return False

    # +  -  -  - MESSAGES DISPLAY -  -  - +

    def display_win_message(self):
        print(MESSAGES['win'].format(self.current_player))

    def display_draw_message(self):
        print(MESSAGES['draw'])

    def display_quit_message(self):
        print(MESSAGES['quit'])

    def display_game_over_message(self):
        print(MESSAGES['game_over'])

    def display_welcome_message(self):
        print(MESSAGES['welcome'])

    def display_coords_existed_message(self):
        print(MESSAGES['coords_existed'])

    # +  -  -  - GAME -  -  - +

    def switch_player(self):
        ''' Toggle current player 1 and 2 '''

        if self.current_player == PLAYER_1:
            self.current_player = PLAYER_2
            self.current_symbol = PLAYER_2_SYMBOL
        else:
            self.current_player = PLAYER_1
            self.current_symbol = PLAYER_1_SYMBOL

    def run_game(self):
        ''' Main function running the game '''

        # welcome players
        self.display_welcome_message()
        # print current board
        self.board.draw_board()

        # while loop to keep the game going
        while not self.game_over:
            # get player input
            intput_prompt = MESSAGES['prompt_input'].format(
                self.current_player, self.current_symbol)

            self.input_coordinates = input(
                intput_prompt).replace(" ", "").split(',')

            if len(self.input_coordinates) == 1:
                if self.input_coordinates[0].lower() == 'q':
                    self.display_quit_message()
                    break

            if self.validate_input():
                # if input coordinates have not existed, insert to board
                if not self.board.have_coords_existed(self.x_input, self.y_input):
                    self.board.insert_move(
                        self.x_input, self.y_input, self.current_symbol)
                else:
                    self.display_coords_existed_message()
                    continue

                # if player manages to fill 1 row/column/diagonal, then win
                if self.board.is_column_filled() \
                        or self.board.is_row_filled() \
                        or self.board.is_diagonal_filled():
                    self.display_win_message()
                    self.game_over = True

                # if no one wins and board is filled, then draw
                if self.board.is_board_filled():
                    self.game_over = True
                    self.display_draw_message()

                # re-draw board
                self.board.draw_board()

                # switch player
                self.switch_player()

            else:
                continue

        self.display_game_over_message()
