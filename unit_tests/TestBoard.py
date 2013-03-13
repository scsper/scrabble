import unittest
from board import Board, BoardPosition
from tile import Tile
from enum import Multiplier, BoardPositionState


class TestSequenceFunctions(unittest.TestCase):
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
        self.b.place_tile(tile, 0, 0)
        self.assertTrue(self.b.board[0][0].state == BoardPositionState.PENDING)
        self.assertTrue(self.b.board[0][0].tile == tile)

if __name__ == '__main__':
    unittest.main()
