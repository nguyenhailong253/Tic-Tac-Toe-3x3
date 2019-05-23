# author: long nguyen (nguyenhailong253@gmail.com)

import unittest
from src.board import Board


class TestBoard(unittest.TestCase):
    ''' Test cases for class Board '''

    def test_insert_O(self):
        ''' If board inserts O in correct coordinates '''

        board = Board()
        board.insert_move(1, 2, 'O')
        self.assertEqual(board.get_board()[1][2], 'O')

    def test_insert_X(self):
        ''' If board inserts X in correct coordinates '''

        board = Board()
        board.insert_move(0, 1, 'X')
        self.assertEqual(board.get_board()[0][1], 'X')

    def test_is_row_filled(self):
        ''' If one of 3 rows is filled, should return True '''

        board = Board()
        board.insert_move(1, 0, 'X')
        board.insert_move(1, 1, 'X')
        board.insert_move(1, 2, 'X')

        self.assertTrue(board.is_row_filled())

    def test_is_column_filled(self):
        ''' If one of 3 columns is filled, should return True '''

        board = Board()
        board.insert_move(0, 2, 'O')
        board.insert_move(1, 2, 'O')
        board.insert_move(2, 2, 'O')

        self.assertTrue(board.is_column_filled())

    def test_is_diagonal_filled(self):
        ''' If one of 2 diagonal is filled, should return True '''

        board = Board()

        # left to right diagonal
        board.insert_move(0, 0, 'O')
        board.insert_move(1, 1, 'O')
        board.insert_move(2, 2, 'O')
        self.assertTrue(board.is_diagonal_filled())

        # right to left diagonal
        board.insert_move(0, 2, 'X')
        board.insert_move(1, 1, 'X')
        board.insert_move(2, 0, 'X')
        self.assertTrue(board.is_diagonal_filled())

    def test_is_board_filled(self):
        ''' If board is all filled, should return True '''

        board = Board()
        self.assertFalse(board.is_board_filled())

        for x in range(3):
            for y in range(3):
                board.insert_move(x, y, 'X')
        self.assertTrue(board.is_board_filled())


if __name__ == "__main__":
    unittest.main()
