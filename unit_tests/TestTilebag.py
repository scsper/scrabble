import unittest
from tilebag import Tilebag

class TestTilebag(unittest.TestCase):
    def test_constructor(self):
        tilebag = Tilebag("../tileset.txt")
        self.assertTrue(len(tilebag.tiles) == 100)




if __name__ == '__main__':
    unittest.main()
