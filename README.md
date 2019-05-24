# Tic-Tac-Toe-3x3
A console based version of Tic Tac Toe that allows two human players to play the game on a 3 x 3 board

## Requirements
- [Python 3.7.x](https://www.python.org/downloads/)

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
- If player wants to quit the game, type 'q', anything else will be invalid
- At the end of each game, players will be asked whether they want to continue with a new round, type 'y' to do so or anything else to exit

### Co-ordinates plane
- The board is 2D with horizontal x-axis and vertical y-axis
- x values increase from left to right, y values increase from top to bottom
- The starting point of the board is on top left with co-ordinates of (1,1), meaning x = y = 1
- The maximum point is (3,3)

## Demo

    Welcome to Tic Tac Toe !

    Player 1 will go first and play 'X'. Please type coordinates of x and y separated by a comma (i.e 1,3 or 2, 2). 
    Otherwise, the inputs will be invalid

    . . .

    . . .

    . . .

    Players 1 enters a coord x,y to place your X or enter 'q' to give up: 1,1

    Move Accepted

    X . .

    . . .

    . . .

    Players 2 enters a coord x,y to place your O or enter 'q' to give up: 3,3

    Move Accepted

    X . .

    . . .

    . . O

    Players 1 enters a coord x,y to place your X or enter 'q' to give up: 2,2

    Move Accepted

    X . .

    . X .

    . . O

    Players 2 enters a coord x,y to place your O or enter 'q' to give up: 3,2

    Move Accepted

    X . .

    . X .

    . O O

    Players 1 enters a coord x,y to place your X or enter 'q' to give up: 1,3

    Move Accepted

    X . X

    . X .

    . O O

    Players 2 enters a coord x,y to place your O or enter 'q' to give up: 3,1

    Move Accepted

    Congratulations ! Player 2 has won the game!

    X . X

    . X .

    O O O

    Game Over!

    Do you want to play again? Type 'y' to do so, or anything else to exit: n
    Thank you for playing TicTacToe. Hope you had a great time!


## Testing (for developers)
Test board component

    python -m unittest tests.test_board

Test game component

    python -m unittest tests.test_game

## Assumptions
- Players can read and understand English and numbers
- Players know how co-ordinates work (that is 1,3 will correspond to row or x = 1 and column or y = 3)
- If player 1 is the winner then player 2 will be the loser, and vice versa
