from enum import Multiplier, BoardPositionState

class Board:
	board = []
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
		build_board(self.board)
		print self.board


	def build_board(board):
		for row in range(15):
			for col in range(15):
				board[row][col] = BoardPosition(board[row][col])


# Board helper class
class BoardPosition:
	def __init__(self, value):
		self.state = BoardPositionState.OPEN	
		if value == 0:
			self.multiplier = Multiplier.NONE
		elif value == 2:
			self.multiplier = Multiplier.DOUBLE_LETTER
		elif value == 3:
			self.multiplier = Multiplier.DOUBLE_WORD
		elif value == 4:
			self.multiplier = Multiplier.TRIPLE_LETTER
		elif value == 5: 
			self.multiplier = Multiplier.TRIPLE_WORD


	def __str__(self):
		return "My multiplier is " + self.multiplier + " and my state is " + self.state



