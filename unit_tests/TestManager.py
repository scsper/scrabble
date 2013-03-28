import unittest
from mock import MagicMock
from board import Board
from tile import Tile
from manager import Manager
from enum import BoardPositionState

class TestManager(unittest.TestCase):
    def setUp(self):
        self.b = Board()
        self.manager = Manager(self.b)


    def test_row_direction(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 1, 2)
        self.b.place_tile(c, 1, 3)
        self.b.place_tile(d, 1, 4)

        self.assertTrue(self.manager.check_direction())


    def test_col_direction(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 2, 1)
        self.b.place_tile(c, 3, 1)
        self.b.place_tile(d, 4, 1)

        self.assertTrue(self.manager.check_direction())


    def test_multi_direction(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 2, 1)
        self.b.place_tile(c, 2, 2)
        self.b.place_tile(d, 2, 3)

        self.assertFalse(self.manager.check_direction())


    def test_connectivity_middle(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)

        self.b.place_tile(a, 2, 1)
        self.b.place_tile(b, 2, 2)
        self.b.place_tile(c, 2, 3)
        self.b.place_tile(d, 2, 4)
        self.b.place_tile(e, 2, 5)

        self.b.board[2][3].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_end(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 2, 1)
        self.b.place_tile(c, 3, 1)
        self.b.place_tile(d, 4, 1)
        self.b.place_tile(e, 5, 1)

        self.b.board[5][1].state = BoardPositionState.FULL
        self.manager.check_direction()

        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_beginning(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 2, 1)
        self.b.place_tile(c, 3, 1)
        self.b.place_tile(d, 4, 1)
        self.b.place_tile(e, 5, 1)

        self.b.board[1][1].state = BoardPositionState.FULL
        self.manager.check_direction()

        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_two_anchor_consecutive(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)


        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 2, 1)
        self.b.place_tile(c, 3, 1)
        self.b.place_tile(d, 4, 1)
        self.b.place_tile(e, 5, 1)
        self.b.place_tile(f, 6, 1)


        self.b.board[3][1].state = BoardPositionState.FULL
        self.b.board[4][1].state = BoardPositionState.FULL
        self.manager.check_direction()

        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_two_anchor_gap(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)

        self.b.place_tile(a, 1, 1)
        self.b.place_tile(b, 1, 2)
        self.b.place_tile(c, 1, 3)
        self.b.place_tile(d, 1, 4)
        self.b.place_tile(e, 1, 5)
        self.b.place_tile(f, 1, 6)

        self.b.board[1][2].state = BoardPositionState.FULL
        self.b.board[1][5].state = BoardPositionState.FULL
        self.manager.check_direction()

        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_gap(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)

        self.b.place_tile(a, 2, 1)
        self.b.place_tile(b, 2, 2)
        self.b.place_tile(c, 2, 3)
        self.b.place_tile(d, 2, 5)
        self.b.place_tile(e, 2, 6)

        self.b.board[2][3].state = BoardPositionState.FULL
        self.manager.check_direction()

        self.assertFalse(self.manager.check_connectivity())


    def test_connectivity_no_anchor(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)

        self.b.place_tile(a, 2, 1)
        self.b.place_tile(b, 2, 2)
        self.b.place_tile(c, 2, 3)
        self.b.place_tile(d, 2, 4)

        self.manager.check_direction()
        self.assertFalse(self.manager.check_connectivity())
