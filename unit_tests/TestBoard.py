import unittest
from board import Board, BoardPosition
from tile import Tile
from enum import Multiplier, BoardPositionState


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_constructor(self):
        tw = BoardPosition(5)
        tl = BoardPosition(4)
        dw = BoardPosition(3)
        dl = BoardPosition(2)
        self.assertTrue(self.b.board[0][0] == tw)
        self.assertTrue(self.b.board[7][7] == dw)
        self.assertTrue(self.b.board[0][3] == dl)
        self.assertTrue(self.b.board[5][1] == tl)


    def test_place_tile(self):
        tile = Tile('a', 1)
        isValid = self.b.place_tile(tile, 0, 0)
        self.assertTrue(self.b.board[0][0].state == BoardPositionState.PENDING)
        self.assertTrue(self.b.board[0][0].tile == tile)
        self.assertTrue(isValid)

        second_tile = Tile('b', 4)
        self.b.board[9][9].state = BoardPositionState.FULL
        isValid = self.b.place_tile(second_tile, 9, 9)
        self.assertTrue(not isValid)

        isValid = self.b.place_tile(second_tile, 0, 0)
        self.assertTrue(not isValid)


    def test_retrieve_tile(self):
        tile = Tile('a', 1)
        self.b.place_tile(tile, 4, 8)

        retrieved = self.b.retrieve_tile(4, 8)
        self.assertTrue(retrieved == tile)
        self.assertTrue(self.b.board[4][8].state == BoardPositionState.EMPTY)
        self.assertTrue(self.b.board[4][8].tile == None)

    def test_retrieve_tile_full(self):
        tile = Tile('a', 1)
        self.b.place_tile(tile, 4, 8)
        self.b.board[4][8].state = BoardPositionState.FULL

        retrieved = self.b.retrieve_tile(4, 8)
        self.assertTrue(not retrieved)


    def test_retrieve_all(self):
        tileA = Tile('a', 1)
        tileB = Tile('b', 4)
        tileC = Tile('c', 3)
        tileD = Tile('d', 2)
        tileE = Tile('e', 1)

        should_retrieve = [tileA, tileB, tileC]

        self.b.place_tile(tileA, 4, 7)
        self.b.place_tile(tileB, 6, 3)
        self.b.place_tile(tileC, 1, 4)
        self.b.place_tile(tileD, 12, 2)
        self.b.place_tile(tileE, 8, 14)

        self.b.board[12][2].state = BoardPositionState.FULL
        self.b.board[8][14].state = BoardPositionState.FULL

        retrieved_tiles = self.b.retrieve_all()

        # should not leave anything that is PENDING -- scan the board for PENDING
        for row in xrange(15):
            for col in xrange(15):
                self.assertTrue(self.b.board[row][col] != BoardPositionState.PENDING)

        # should not retrieve FULL tiles or reset its tiles to None
        self.assertTrue(self.b.board[12][2].state == BoardPositionState.FULL)
        self.assertTrue(self.b.board[12][2].tile == tileD)

        self.assertTrue(self.b.board[8][14].state == BoardPositionState.FULL)
        self.assertTrue(self.b.board[8][14].tile == tileE)

        # any space that was PENDING should now be EMPTY
        self.assertTrue(self.b.board[4][7].state == BoardPositionState.EMPTY)
        self.assertTrue(self.b.board[6][3].state == BoardPositionState.EMPTY)
        self.assertTrue(self.b.board[1][4].state == BoardPositionState.EMPTY)

        # any space that was PENDING should now have None tile
        self.assertTrue(self.b.board[4][7].tile == None)
        self.assertTrue(self.b.board[6][3].tile == None)
        self.assertTrue(self.b.board[1][4].tile == None)

        # should return an array of tiles that were on the board
        self.assertTrue(len(should_retrieve) == len(retrieved_tiles))
        for tile in should_retrieve:
            found_index = retrieved_tiles.index(tile)
            found_tile = retrieved_tiles.pop(found_index)
            self.assertTrue(found_tile == tile)


if __name__ == '__main__':
    unittest.main()
