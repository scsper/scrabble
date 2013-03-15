import unittest
from tilebag import Tilebag

class TestTilebag(unittest.TestCase):
    def setUp(self):
        self.tilebag = Tilebag("mocks/mockTileset.txt")


    def test_constructor(self):
        a = 0
        b = 0
        c = 0
        for tile in self.tilebag.tiles:
            if tile.letter == 'a' and tile.points == 1:
                a += 1
            elif tile.letter == 'b' and tile.points == 3:
                b += 1
            elif tile.letter == 'c' and tile.points == 2:
                c += 1
            else:
                self.assertTrue(True == False, "ERROR: invalid letter and point combination")

        self.assertTrue(len(self.tilebag.tiles) == 6, "ERROR: wrong number of tiles read in from file")
        self.assertTrue(a == 2, "ERROR: wrong number of As")
        self.assertTrue(b == 1, "ERROR: wrong number of Bs")
        self.assertTrue(c == 3, "ERROR: wrong number of Cs")


    def test_draw(self):
        a = 0
        b = 0
        c = 0

        drawnTiles = self.tilebag.draw(4)

        for tile in drawnTiles:
            if tile.letter == 'a':
                a += 1
            elif tile.letter == 'b':
                b += 1
            elif tile.letter == 'c':
                c += 1
            else:
                self.assertTrue(True == False, "ERROR: invalid letter drawn from the tilebag")

        for tile in self.tilebag.tiles:
            if tile.letter == 'a':
                a += 1
            elif tile.letter == 'b':
                b += 1
            elif tile.letter == 'c':
                c += 1
            else:
                self.assertTrue(True == False, "ERROR: invalid letter drawn from the tilebag")

        self.assertTrue(a == 2, "ERROR: wrong number of As")
        self.assertTrue(b == 1, "ERROR: wrong number of Bs")
        self.assertTrue(c == 3, "ERROR: wrong number of Cs")

        self.assertTrue(len(drawnTiles) == 4, "ERROR: wrong number of tiles returned")
        self.assertTrue(len(self.tilebag.tiles) == 2, "ERROR: wrong number of tiles left in tilebag")


    def test_draw_end_tilebag(self):
        drawnTiles = self.tilebag.draw(7)

        for tile in drawnTiles:
            if tile.letter == 'a':
                a += 1
            elif tile.letter == 'b':
                b += 1
            elif tile.letter == 'c':
                c += 1
            else:
                self.assertTrue(True == False, "ERROR: invalid letter drawn from the tilebag")

        self.assertTrue(a == 2, "ERROR: wrong number of As")
        self.assertTrue(b == 1, "ERROR: wrong number of Bs")
        self.assertTrue(c == 3, "ERROR: wrong number of Cs")

        self.assertTrue(len(drawnTiles) == 6, "ERROR: there should only be 6 tiles in the tilebag right now")
        self.assertTrue(len(self.tilebag.tiles) == 0, "ERROR: there should be no more tiles in the tilebag right now")


    def test_swap(self):
        d = Tile('d', 2)
        e = Tile('e', 1)
        swapTiles = [d, e]
        drawnTiles = self.tilebag.swap(swapTiles)

        self.assertTrue(len(drawnTiles) == 2, "ERROR: tiles that the user gets in return should match the number swapped")

        self.assertTrue(self.tilebag.tiles.index(d) > -1, "ERROR: d was not found in the tilebag")
        self.assertTrue(self.tilebag.tiles.index(e) > -1, "ERROR: e was not found in the tilebag")


    def test_swap_end_tilebag(self):
        d = Tile('d', 2)
        e = Tile('e', 1)
        f = Tile('f', 4)
        g = Tile('g', 3)
        h = Tile('h', 4)
        i = Tile('i', 1)
        j = Tile('j', 8)

        swapTiles = [d, e, f, g, h, i, j]
        drawnTiles = self.tilebag.swap(swapTiles)

        self.assertTrue(len(drawnTiles) == 0, "ERROR: when swapTiles > num of tiles in the bag, you should not draw tiles")
        self.assertTrue(True == False, "ERROR: place holder for figuring out what to return in this case"





if __name__ == '__main__':
    unittest.main()
