class Tilebag(object):
	def __init__(self):
		self.tiles = []
		with open("tileset.txt") as f:
			for line in f:
				line = split(line)
				letter = line[0]
				freq = line[1]
				points = line[2]

				for i in xrange(freq):
					print letter + ' ' + points
					self.tiles.append(Tile(letter, int(points)))