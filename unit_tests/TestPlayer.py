import unittest
from mock import MagicMock
from board import Board
from player import Player
from tile import Tile

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Scott", self.board)


    def test_constructor(self):
        self.assertTrue(self.player.name == "Scott", "The player's name is not being set correctly.")
        self.assertTrue(self.player.points == 0, "The player's points should be set to 0.")
        self.assertTrue(self.player.rack == [], "The player's rack should be empty.")
        self.assertTrue(self.board == self.player.board, "The player did not store the correct reference to the board.")


    def test_play_success(self):
        tile = Tile('a', 1)
        second_tile = Tile('b', 4)

        self.player.rack.append(tile)
        self.player.rack.append(second_tile)

        self.board.place_tile = MagicMock(return_value=True)
        self.player.place(tile, 1, 1)
        self.board.place_tile.assert_called_with(tile, 1, 1)
        self.assertTrue(len(self.player.rack) == 1)
        self.assertTrue(self.player.rack.index(second_tile) == 0)


    def test_play_failure(self):
        tile = Tile('a', 1)
        second_tile = Tile('b', 4)

        self.player.rack.append(tile)
        self.player.rack.append(second_tile)

        self.board.place_tile = MagicMock(return_value=False)
        self.player.place(tile, 1, 1)
        self.board.place_tile.assert_called_with(tile, 1, 1)
        self.assertTrue(len(self.player.rack) == 2)


    def test_retrieve_success(self):
        tile = Tile('a', 1)

        self.board.retrieve_tile = MagicMock(return_value=tile)
        self.player.retrieve_tile(1, 1)

        self.board.retrieve_tile.assert_called_with(1, 1)

        self.assertTrue(len(self.player.rack) == 1)
        self.assertTrue(self.player.rack.index(tile) == 0)


    def test_retrieve_failure(self):
        tile = Tile('a', 1)

        self.board.retrieve_tile = MagicMock(return_value=False)
        self.player.retrieve_tile(1, 1)

        self.board.retrieve_tile.assert_called_with(1, 1)

        self.assertTrue(len(self.player.rack) == 0)
        with self.assertRaises(ValueError):
            self.player.rack.index(tile)


    def test_retrieve_all(self):
        tileA = Tile('a', 1)
        tileB = Tile('b', 1)
        tileC = Tile('c', 1)
        tileD = Tile('d', 1)

        tiles = [tileA, tileB, tileC]
        self.player.rack.append(tileD)

        self.board.retrieve_all = MagicMock(return_value=tiles)
        self.player.retrieve_all()

        self.assertTrue(len(self.player.rack) == 4)
        self.assertTrue(self.player.rack.index(tileB)) # should return something, not throw an exception












if __name__ == '__main__':
    unittest.main()
