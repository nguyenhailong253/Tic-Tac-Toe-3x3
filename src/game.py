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
        # first player is always X
        self.current_player = PLAYER_1
        self.current_symbol = PLAYER_1_SYMBOL

        self.board = Board()
        self.msg = Messages()

        # user input x,y coordinates
        self.input_coordinates = []
        self.x_input = None
        self.y_input = None

        # game over flag
        self.game_over = False
        self.quit_game = False

    # +  -  -  - INPUT VALIDATION -  -  - +

    def is_input_numerical(self, x_input, y_input):
        ''' Check if x,y are numerical '''
        return x_input.isnumeric() and y_input.isnumeric()

    def is_input_within_range(self, x_input, y_input):
        ''' Check if x,y are within range 1 to 3 '''

        valid_range = range(1, 4)  # from 1 to 3
        if x_input in valid_range and y_input in valid_range:
            return True
        return False

    def validate_input(self):
        ''' Validate if input is numerical and within range '''

        if len(self.input_coordinates) == 2:
            # deconstruct list of inputs - currently type string
            x_input = self.input_coordinates[0]
            y_input = self.input_coordinates[1]

            if self.is_input_numerical(x_input, y_input):
                # if inputs are numerical, convert to integers
                x_input = int(x_input)
                y_input = int(y_input)

                if self.is_input_within_range(x_input, y_input):
                    self.x_input = x_input - 1
                    self.y_input = y_input - 1
                    return True
                else:
                    self.msg.display_out_of_range_message()
            else:
                self.msg.display_wrong_type_message()
        else:
            self.msg.display_wrong_num_inputs_message()

        return False

    # +  -  -  - GAME -  -  - +

    def restart_game(self):
        ''' Reset all fields '''

        # first player is always X
        self.current_player = PLAYER_1
        self.current_symbol = PLAYER_1_SYMBOL

        self.board = Board()
        self.msg = Messages()

        # user input x,y coordinates
        self.input_coordinates = []
        self.x_input = None
        self.y_input = None

        # game over flag
        self.game_over = False
        self.quit_game = False

    def switch_player(self):
        ''' Toggle current player 1 and 2 '''

        if self.current_player == PLAYER_1:
            self.current_player = PLAYER_2
            self.current_symbol = PLAYER_2_SYMBOL
        else:
            self.current_player = PLAYER_1
            self.current_symbol = PLAYER_1_SYMBOL

    def check_board_condition(self):
        ''' Check if board or row/column/diagonal is filled '''

        # if player manages to fill 1 row/column/diagonal, then win
        if self.board.is_column_filled() \
                or self.board.is_row_filled() \
                or self.board.is_diagonal_filled():
            self.msg.display_win_message(self.current_player)
            self.game_over = True

        # if no one wins and board is filled, then draw
        if self.board.is_board_filled():
            self.game_over = True
            self.msg.display_draw_message()

    def play(self):
        ''' Continuously asking player for inputs to carry out the game '''

        # welcome players
        self.msg.display_welcome_message()
        self.msg.display_instructions()
        # print current board
        self.board.draw_board()

        # while game_over flag is still false
        while not self.game_over:
            # get player input
            intput_prompt = self.msg.get_prompt_input(
                self.current_player, self.current_symbol)

            self.input_coordinates = input(
                intput_prompt).replace(" ", "").split(',')

            # check if player types 'q'
            if len(self.input_coordinates) == 1:
                if self.input_coordinates[0].lower() == 'q':
                    self.msg.display_quit_message()
                    self.quit_game = True
                    break

            if self.validate_input():
                # if input coordinates have not existed, insert to board
                if not self.board.have_coords_existed(self.x_input, self.y_input):
                    self.msg.display_valid_input_message()
                    self.board.insert_move(
                        self.x_input, self.y_input, self.current_symbol)
                else:
                    self.msg.display_coords_existed_message()
                    continue  # try again

                self.check_board_condition()

                # re-draw board
                self.board.draw_board()

                # switch player
                self.switch_player()

        self.msg.display_game_over_message()

    def run(self):
        ''' Main function runnning the game '''

        while True:
            self.restart_game()
            self.play()

            if self.quit_game:
                break

            # ask players to type 'y' if they want to play again
            play_again = input(self.msg.get_play_again_message()).strip()

            if play_again.lower() != 'y':
                break

        self.msg.display_thank_message()
