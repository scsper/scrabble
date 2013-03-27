from enum import Multiplier, BoardPositionState
from board import Board

# enforces game logic
class Manager(object):
    def __init__(self, board):
        self.b = board
        self.xytiles = [] # a list of tuples containing the tile and xy coordinates of every thing played this turn

    def get_tiles_and_positions(self):
        self.xytiles = []

        for row in xrange(15):
            for col in xrange(15):
                if(self.b.board[row][col].state == BoardPositionState.PENDING):
                    tile = self.b.board[row][col].tile
                    self.xytiles.append((tile, row, col))


    def check_direction(self):
        self.row, self.col = True, True

        self.get_tiles_and_positions()

        if(not self.xytiles): # empty array... should never happen, but when it does.....
            return False;
        else:
            tiles, xCoords, yCoords = zip(*self.xytiles) # unzip the tuple

            for x in xCoords:
                if(x != xCoords[0]):
                    self.row = False

            for y in yCoords:
                if(y != yCoords[0]):
                    self.col = False

        return (self.row or self.col)


    def check_connectivity(self):
        tiles, xCoords, yCoords = zip(*self.xytiles) # unzip the tuple
        if(self.row):


    def _check_gaps(self, coords):
        valCheck = coords[0]

        for c in len(coords):
            if(valCheck != coords[c]):

                # go find it on the board sucka
                # if it is empty, that's the end of the word.  if there is more to look at, it's wrong
                # if it is full, then you just found your anchor
            valCheck += 1



