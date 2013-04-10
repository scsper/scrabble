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
        foundAnchor = False

        if(self.row):
            row = xCoords[0]
            gaps = self._find_gaps(yCoords)

            if(gaps is not None):
                for col in gaps:
                    if(self.b.board[row][col].state == BoardPositionState.FULL):
                        foundAnchor = True
                    else: # the board position is empty, meaning that there is a gap.  this invalidates the move.
                        return False

            if(not foundAnchor):
                if(yCoords[0] != 0): # don't go off the top of the board
                    if(self.b.board[row][yCoords[0] - 1].state == BoardPositionState.FULL):
                        foundAnchor = True

                if(yCoords[-1] != 14): # don't go off the bottom of the board
                    if(self.b.board[row][yCoords[-1] + 1].state == BoardPositionState.FULL):
                        foundAnchor = True

            return foundAnchor
        else:
            col = yCoords[0]
            gaps = self._find_gaps(xCoords)

            if(gaps is not None):
                for row in gaps:
                    if(self.b.board[row][col].state == BoardPositionState.FULL):
                        foundAnchor = True
                    else: # the board position is empty, meaning that there is a gap.  this invalidates the move.
                        return False

            if(not foundAnchor):
                if(xCoords[0] != 0): # don't go off the top of the board
                    if(self.b.board[xCoords[0] - 1][col].state == BoardPositionState.FULL):
                        foundAnchor = True

                if(xCoords[-1] != 14): # don't go off the bottom of the board
                    if(self.b.board[xCoords[-1] + 1][col].state == BoardPositionState.FULL):
                        foundAnchor = True

            return foundAnchor


    def _find_gaps(self, coords):
        first = coords[0]
        gaps = []

        for c in xrange(len(coords)):
            while (first != coords[c]):
                gaps.append(first)
                first += 1
            first += 1

        return gaps


    def _scan(self, direction, x, y):
        word = ""

        if direction is 'up':
            while( x != 0 and self.b.board[x - 1][y].state is not BoardPositionState.EMPTY):
                x -= 1
                word = self.b.board[x][y].tile.letter + word # put it at the beginning of the string
        elif direction is 'down':
            while( x != 14 and self.b.board[x + 1][y].state is not BoardPositionState.EMPTY):
                x += 1
                word = word + self.b.board[x][y].tile.letter # put it at the end of string
        elif direction is 'left':
            while( y != 0 and self.b.board[x][y - 1].state is not BoardPositionState.EMPTY):
                y -= 1
                word = self.b.board[x][y].tile.letter + word # put it at the beginning of the string
        elif direction is 'right':
            while( y != 14 and self.b.board[x][y + 1].state is not BoardPositionState.EMPTY):
                y += 1
                word = word + self.b.board[x][y].tile.letter # put it at end of the string
        else:
            assert(false, "invalid direction passed into '_scan()'.  value should be up down left or right.")

        return word


    def form_words(self):
        tiles, xCoords, yCoords = zip(*self.xytiles) # unzip the tuple
        words = []
        y = yCoords[0]
        x = xCoords[0]

        if(self.row):
            anchorWord = self._scan('left', x, y) + tiles[0].letter + self._scan('right', x, y)

            for y in yCoords:
                tempWord = self._scan('up', x, y) + self.b.board[x][y].tile.letter + self._scan('down', x, y)

                if(len(tempWord) > 1):
                    words.append(tempWord)
        else:
            anchorWord = self._scan('up', x, y) + tiles[0].letter + self._scan('down', x, y)

            for x in xCoords:
                tempWord = self._scan('left', x, y) + self.b.board[x][y].tile.letter + self._scan('right', x, y)

                if(len(tempWord) > 1):
                    words.append(tempWord)


        words.append(anchorWord)
        return words
