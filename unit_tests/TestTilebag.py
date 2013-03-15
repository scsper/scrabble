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


    def test_draw_end_of_tilebag(self):
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
        drawnTiles = self.tilebag.swap(tiles)
        # pass in a list of tiles
            # check that those tiles get placed into the tilebag
        # get the same number of tiles in return


if __name__ == '__main__':
    unittest.main()
