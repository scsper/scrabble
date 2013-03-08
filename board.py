from enum import Multiplier, BoardPositionState

class Board(object):
	def __init__(self):
		self.board = [
						[5,0,0,2,0,0,0,5,0,0,0,2,0,0,5],
						[0,3,0,0,0,4,0,0,0,4,0,0,0,3,0],
						[0,0,3,0,0,0,2,0,2,0,0,0,3,0,0],
						[2,0,0,3,0,0,0,2,0,0,0,3,0,0,2],
						[0,0,0,0,3,0,0,0,0,0,3,0,0,0,0],
						[0,4,0,0,0,4,0,0,0,4,0,0,0,4,0],
						[0,0,2,0,0,0,2,0,2,0,0,0,2,0,0],
						[5,0,0,2,0,0,0,3,0,0,0,2,0,0,5],
						[0,0,2,0,0,0,2,0,2,0,0,0,2,0,0],
						[0,4,0,0,0,4,0,0,0,4,0,0,0,4,0],
						[0,0,0,0,3,0,0,0,0,0,3,0,0,0,0],
						[2,0,0,3,0,0,0,2,0,0,0,3,0,0,0],
						[0,0,3,0,0,0,2,0,2,0,0,0,3,0,0],
						[0,3,0,0,0,4,0,0,0,4,0,0,0,3,0],
						[5,0,0,2,0,0,0,5,0,0,0,2,0,0,5]
					]
		self.build_board()
		print self.board


	def place_tile(self, tile, row, col):
		self.board[row][col].state = BoardPosition.PENDING
		self.board[row][col].tile = tile


	def build_board(self):
		for row in xrange(15):
			for col in xrange(15):
				self.board[row][col] = BoardPosition(self.board[row][col])


# Board helper class
class BoardPosition(object):
	def __init__(self, value):
		self.state = BoardPositionState.EMPTY
		self.tile = None

		if value == 0:
			self.name = "NONE"
			self.multiplier = Multiplier.NONE
		elif value == 2:
			self.name = "DOUBLE_LETTER"
			self.multiplier = Multiplier.DOUBLE_LETTER
		elif value == 3:
			self.name = "DOUBLE_WORD"
			self.multiplier = Multiplier.DOUBLE_WORD
		elif value == 4:
			self.name = "TRIPLE_LETTER"
			self.multiplier = Multiplier.TRIPLE_LETTER
		elif value == 5: 
			self.name = "TRIPLE_WORD"
			self.multiplier = Multiplier.TRIPLE_WORD

	def __str__(self):
		return self.name + " state: " + str(self.state)
