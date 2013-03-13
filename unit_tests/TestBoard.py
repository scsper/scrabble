import unittest
from board import Board
from tile import Tile


class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_constructor(self):
		self.board.place_tile(Tile('a', 1), 0, 0)
		self.board.assertTrue(1 == 1)

if __name__ == '__main__':
	unittest.main()
