# author: long nguyen (nguyenhailong253@gmail.com)

MSG = {
    "win": "Congratulations ! Player {} has won the game!\n",
    "draw": "Draw match!\n",
    "quit": "You have quitted the game.\n",
    "welcome": "Welcome to Tic Tac Toe !\n",
    "valid_input": "\nMove Accepted\n",
    "prompt_input": "Players {} enters a coord x,y to place your {} or enter 'q' to give up: ",
    "wrong_type": "Inputs are not numerical. Please try again\n",
    "out_of_range": "Inputs are out of range (1,3). Please try again\n",
    "wrong_num_inputs": "Too many/few inputs. Please try again\n",
    "coords_existed": "Oh no, a piece is already at this place! Please try again\n",
    "game_over": "Game Over!\n",
    "instructions": "Player 1 will go first and play 'X'. Please type in the coordinates of x and y separated by a comma (i.e 1,3 or 2, 2). \nOtherwise, the inputs will be invalid\n",
    "play_again": "Do you want to play again? Type 'y' to do so, or anything else to exit: ",
    "thank_player": "\nThank you for playing TicTacToe. Hope you had a great time!\n"
}


class Messages(object):
    ''' Displayer of different messages '''

    # +  -  -  - GREETINGS -  -  - +

    def display_welcome_message(self):
        print(MSG['welcome'])

    def display_instructions(self):
        print(MSG['instructions'])

    def display_thank_message(self):
        print(MSG['thank_player'])

    # +  -  -  - GAME STATUS -  -  - +

    def display_win_message(self, current_player):
        print(MSG['win'].format(current_player))

    def display_draw_message(self):
        print(MSG['draw'])

    def display_quit_message(self):
        print(MSG['quit'])

    def display_game_over_message(self):
        print(MSG['game_over'])

    # +  -  -  - INPUT VALIDATION -  -  - +

    def display_valid_input_message(self):
        print(MSG['valid_input'])

    def display_coords_existed_message(self):
        print(MSG['coords_existed'])

    def display_out_of_range_message(self):
        print(MSG['out_of_range'])

    def display_wrong_type_message(self):
        print(MSG['wrong_type'])

    def display_wrong_num_inputs_message(self):
        print(MSG['wrong_num_inputs'])

    # +  -  -  - GETTER METHOD -  -  - +

    def get_prompt_input(self, player, symbol):
        return MSG['prompt_input'].format(player, symbol)

    def get_play_again_message(self):
        return MSG['play_again']
