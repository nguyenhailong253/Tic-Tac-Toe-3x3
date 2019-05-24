# Tic-Tac-Toe-3x3
A console based version of Tic Tac Toe that allows two human players to play the game on a 3 x 3 board

## Requirements
- Python 3.6.x

## Running the game

    git clone https://github.com/nguyenhailong253/Tic-Tac-Toe-3x3.git
    python tictactoe.py

## Rules

### Game flow
- Two human players are required for the game
- First player will be X and always start the game, second player will be O
- Players take turn to insert their X or O into proper coordinates on the board
- Player wins only when all fields in a column, or a row, or a diagonal are taken by the player
- The game is drawn when all fields are taken on the board

### Input format
- The input coordinates should be 2 integers separated by a comma and within the range of (1,3) (i.e 1,3 or 2,2 or 2,1). Any other formats will be invalid
- If player wants to quit the game, type 'q'
- At the end of each game, players will be asked whether they want to continue with a new round, type 'y' to do so or anything else to exit

## Testing (for developers)
Test board component

    python -m unittest tests.test_board

Test game component

    python -m unittest tests.test_game

## Assumptions