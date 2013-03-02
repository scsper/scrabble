from enum import Multiplier, BoardPositionState

class Board:
	board = [[0 for col in range(15)] for row in range(15)]

	def __init__(self):
		print board


# Board helper class
class BoardPosition:
	def __init__(self):
		multiplier = Multiplier.NONE
		state = BoardPositionState.OPEN

	def __str__(self):
		return "My multiplier is " + self.multiplier + " and my state is " + self.state



