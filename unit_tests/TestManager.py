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

    def test_connectivity_top(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)
        g = Tile('g', 7)
        h = Tile('h', 8)

        self.b.place_tile(a, 2, 1)
        self.b.place_tile(b, 2, 2)
        self.b.place_tile(c, 2, 3)
        self.b.place_tile(d, 2, 4)
        self.b.place_tile(e, 2, 5)

        self.b.place_tile(f, 1, 5)
        self.b.place_tile(g, 1, 6)
        self.b.place_tile(h, 1, 7)

        self.b.board[2][1].state = BoardPositionState.FULL
        self.b.board[2][2].state = BoardPositionState.FULL
        self.b.board[2][3].state = BoardPositionState.FULL
        self.b.board[2][4].state = BoardPositionState.FULL
        self.b.board[2][5].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.assertTrue(self.manager.check_connectivity())

    def test_connectivity_bottom(self):
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)
        g = Tile('g', 7)
        h = Tile('h', 8)

        self.b.place_tile(c, 2, 3)
        self.b.place_tile(d, 2, 4)
        self.b.place_tile(e, 2, 5)

        self.b.place_tile(f, 3, 1)
        self.b.place_tile(g, 3, 2)
        self.b.place_tile(h, 3, 3)

        self.b.board[2][3].state = BoardPositionState.FULL
        self.b.board[2][4].state = BoardPositionState.FULL
        self.b.board[2][5].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.assertTrue(self.manager.check_connectivity())

    def test_connectivity_right(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)
        g = Tile('g', 7)
        h = Tile('h', 8)

        self.b.place_tile(a, 3, 4)
        self.b.place_tile(b, 4, 4)
        self.b.place_tile(c, 5, 4)
        self.b.place_tile(d, 6, 4)
        self.b.place_tile(e, 7, 4)

        self.b.place_tile(f, 1, 5)
        self.b.place_tile(g, 2, 5)
        self.b.place_tile(h, 3, 5)

        self.b.board[3][4].state = BoardPositionState.FULL
        self.b.board[4][4].state = BoardPositionState.FULL
        self.b.board[5][4].state = BoardPositionState.FULL
        self.b.board[6][4].state = BoardPositionState.FULL
        self.b.board[7][4].state = BoardPositionState.FULL

        self.manager.check_direction()

        self.assertTrue(self.manager.check_connectivity())


    def test_connectivity_left(self):
        a = Tile('a', 1)
        b = Tile('b', 2)
        c = Tile('c', 3)
        d = Tile('d', 4)
        e = Tile('e', 5)
        f = Tile('f', 6)
        g = Tile('g', 7)
        h = Tile('h', 8)

        self.b.place_tile(a, 3, 4)
        self.b.place_tile(b, 4, 4)
        self.b.place_tile(c, 5, 4)
        self.b.place_tile(d, 6, 4)
        self.b.place_tile(e, 7, 4)

        self.b.place_tile(f, 7, 3)
        self.b.place_tile(g, 8, 3)
        self.b.place_tile(h, 9, 3)

        self.b.board[3][4].state = BoardPositionState.FULL
        self.b.board[4][4].state = BoardPositionState.FULL
        self.b.board[5][4].state = BoardPositionState.FULL
        self.b.board[6][4].state = BoardPositionState.FULL
        self.b.board[7][4].state = BoardPositionState.FULL

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


    def test_word_row(self):
        b = Tile('b', 3)
        a = Tile('a', 1)
        d = Tile('d', 2)
        g = Tile('g', 2)
        e = Tile('e', 1)
        r = Tile('r', 1)
        ee = Tile('e', 1)
        m = Tile('m', 3)

        self.b.place_tile(b, 6, 4)
        self.b.place_tile(a, 7, 4)
        self.b.place_tile(d, 8, 4)
        self.b.place_tile(g, 9, 4)
        self.b.place_tile(e, 10, 4)
        self.b.place_tile(r, 7, 2)
        self.b.place_tile(ee, 7, 3)
        self.b.place_tile(m, 7, 5)

        self.b.board[6][4].state = BoardPositionState.FULL
        self.b.board[7][4].state = BoardPositionState.FULL
        self.b.board[8][4].state = BoardPositionState.FULL
        self.b.board[9][4].state = BoardPositionState.FULL
        self.b.board[10][4].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.manager.check_connectivity()

        wordsAndPoints = self.manager.form_words()
        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 1, "There should have only been one word found")
        self.assertTrue(words[0] == "ream", "'ream' was not found")


    def test_word_col(self):
        s = Tile('s', 1)
        a = Tile('a', 1)
        g = Tile('g', 2)
        e = Tile('e', 1)
        d = Tile('d', 2)
        r = Tile('r', 1)
        aa = Tile('a', 1)
        m = Tile('m', 3)

        self.b.place_tile(s, 9, 4)
        self.b.place_tile(a, 9, 5)
        self.b.place_tile(g, 9, 6)
        self.b.place_tile(e, 9, 7)
        self.b.place_tile(d, 7, 7)
        self.b.place_tile(r, 8, 7)
        self.b.place_tile(aa, 10, 7)
        self.b.place_tile(m, 11, 7)

        self.b.board[9][4].state = BoardPositionState.FULL
        self.b.board[9][5].state = BoardPositionState.FULL
        self.b.board[9][6].state = BoardPositionState.FULL
        self.b.board[9][7].state = BoardPositionState.FULL


        self.manager.check_direction()
        self.manager.check_connectivity()
        wordsAndPoints = self.manager.form_words()

        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 1, "There should have only been one word found")
        self.assertTrue(words[0] == "dream", "'dream' was not found")


    def test_word_add_s(self):
        a = Tile('a', 1)
        g = Tile('g', 2)
        e = Tile('e', 1)

        r = Tile('r', 1)
        u = Tile('u', 1)
        s = Tile('s', 1)
        ee = Tile('e', 1)

        self.b.place_tile(a, 6, 5)
        self.b.place_tile(g, 6, 6)
        self.b.place_tile(e, 6, 7)

        self.b.place_tile(r, 4, 8)
        self.b.place_tile(u, 5, 8)
        self.b.place_tile(s, 6, 8)
        self.b.place_tile(ee, 7, 8)

        self.b.board[6][5].state = BoardPositionState.FULL
        self.b.board[6][6].state = BoardPositionState.FULL
        self.b.board[6][7].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.manager.check_connectivity()
        wordsAndPoints = self.manager.form_words()
        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 2, "There should have been two words found")
        self.assertTrue(words[0] == "ages", "'ages' was not found")
        self.assertTrue(words[1] == "ruse", "'ruse' was not found")


    def test_word_add_prefix(self):
        a = Tile('a', 1)
        g = Tile('g', 2)
        e = Tile('e', 1)

        r = Tile('r', 1)
        u = Tile('u', 1)
        s = Tile('s', 1)
        t = Tile('t', 1)

        self.b.place_tile(a, 6, 3)
        self.b.place_tile(g, 7, 3)
        self.b.place_tile(e, 8, 3)

        self.b.place_tile(r, 5, 3)
        self.b.place_tile(u, 5, 4)
        self.b.place_tile(s, 5, 5)
        self.b.place_tile(t, 5, 6)

        self.b.board[6][3].state = BoardPositionState.FULL
        self.b.board[7][3].state = BoardPositionState.FULL
        self.b.board[8][3].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.manager.check_connectivity()
        wordsAndPoints = self.manager.form_words()
        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 2, "There should have been two words found")
        self.assertTrue(words[0] == "rage", "'rage' was not found")
        self.assertTrue(words[1] == "rust", "'rust' was not found")


    def test_word_multi_connection(self):
        g = Tile('g', 2)
        r = Tile('r', 1)
        a = Tile('a', 1)
        t = Tile('t', 1)
        e = Tile('e', 1)

        h = Tile('h', 4)
        o = Tile('o', 1)
        s = Tile('s', 1)
        ee = Tile('e', 1)

        self.b.place_tile(g, 8, 3)
        self.b.place_tile(r, 8, 4)
        self.b.place_tile(a, 8, 5)
        self.b.place_tile(t, 8, 6)
        self.b.place_tile(e, 8, 7)

        self.b.place_tile(h, 9, 5)
        self.b.place_tile(o, 9, 6)
        self.b.place_tile(s, 9, 7)
        self.b.place_tile(e, 9, 8)

        self.b.board[8][3].state = BoardPositionState.FULL
        self.b.board[8][4].state = BoardPositionState.FULL
        self.b.board[8][5].state = BoardPositionState.FULL
        self.b.board[8][6].state = BoardPositionState.FULL
        self.b.board[8][7].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.manager.check_connectivity()
        wordsAndPoints = self.manager.form_words()
        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 4, "There should have been four words found")
        self.assertTrue(words[0] == "ah", "'ah' was not found")
        self.assertTrue(words[1] == "to", "'to' was not found")
        self.assertTrue(words[2] == "es", "'es' was not found")
        self.assertTrue(words[3] == "hose", "'hose' was not found")


    def test_word_attach(self):
        r = Tile('r', 1)
        a = Tile('a', 1)
        n = Tile('n', 1)
        k = Tile('k', 5)

        i = Tile('i', 1)
        n = Tile('n', 1)
        g = Tile('g', 2)

        self.b.place_tile(r, 5, 4)
        self.b.place_tile(a, 5, 5)
        self.b.place_tile(n, 5, 6)
        self.b.place_tile(k, 5, 7)
        self.b.place_tile(i, 5, 8)
        self.b.place_tile(n, 5, 9)
        self.b.place_tile(g, 5, 10)

        self.b.board[5][4].state = BoardPositionState.FULL
        self.b.board[5][5].state = BoardPositionState.FULL
        self.b.board[5][6].state = BoardPositionState.FULL
        self.b.board[5][7].state = BoardPositionState.FULL

        self.manager.check_direction()
        self.manager.check_connectivity()

        wordsAndPoints = self.manager.form_words()
        words, points, garbage = zip(*wordsAndPoints) # unzip the tuple

        self.assertTrue(len(words) == 1, "There should have only been one word found")
        self.assertTrue(words[0] == "ranking", "'ranking' was not found")

