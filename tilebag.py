from tile import Tile
from random import shuffle
from enum import ErrorCodes


class Tilebag(object):
	def __init__(self, filepath):
		self.tiles = []
		with open(filepath) as f:
			for line in f:
				line = line.split()
				letter = line[0]
				freq = line[1]
				points = line[2]
				for i in xrange(int(freq)):
					self.tiles.append(Tile(letter, int(points)))

		shuffle(self.tiles)


	def draw(self, numToDraw):
		drawnTiles = []
		for i in xrange(numToDraw):
			if(len(self.tiles) > 0):
				drawnTiles.append(self.tiles.pop())
			else:
				break

		return drawnTiles


	def swap(self, swappedTiles):
		num = len(swappedTiles)

		if(num > len(self.tiles)):
			return ErrorCodes.SWAP

		returnedTiles = self.draw(num)

		self.tiles.extend(swappedTiles)
		shuffle(self.tiles)

		return returnedTiles


	def print_tilebag(self):
		for tile in self.tiles:
			print tile

