import unittest
from tile import Tile


class TestTile(unittest.TestCase):
    def test_constructor(self):
        tile = Tile('a', 1)

        self.assertTrue(tile.letter == 'a')
        self.assertTrue(tile.points == 1)


if __name__ == '__main__':
    unittest.main()
