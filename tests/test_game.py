# author: long nguyen (nguyenhailong253@gmail.com)

import unittest
from src.game import Game


class TestGame(unittest.TestCase):
    ''' Test cases for class Game '''

    def test_numerical_input(self):
        ''' Test if input is numerical '''

        game = Game()
        self.assertTrue(game.is_input_numerical(1, 5))
        self.assertFalse(game.is_input_numerical(1, "5"))
        self.assertFalse(game.is_input_numerical(1, "Hello"))
        self.assertFalse(game.is_input_numerical("", ""))

    def test_out_of_range_input(self):
        ''' Test if input is within 1 to 3 '''

        game = Game()
        self.assertTrue(game.is_input_within_range(1, 3))
        self.assertFalse(game.is_input_within_range(0, 3))
        self.assertFalse(game.is_input_within_range(-3, 1000))


if __name__ == "__main__":
    unittest.main()
