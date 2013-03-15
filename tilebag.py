from tile import Tile
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
