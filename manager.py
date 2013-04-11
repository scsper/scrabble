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
                        return True

                if(yCoords[-1] != 14): # don't go off the bottom of the board
                    if(self.b.board[row][yCoords[-1] + 1].state == BoardPositionState.FULL):
                        return True

                for col in yCoords:
                    if(self._scan('up', row, col) or self._scan('down', row, col)):
                        return True

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

                for row in xCoords:
                    if(self._scan('up', row, col) or self._scan('down', row, col)):
                        return True

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
        tiles = []

        if direction is 'up':
            while( x != 0 and self.b.board[x - 1][y].state is not BoardPositionState.EMPTY):
                x -= 1
                tiles.insert(0, self.b.board[x][y].tile)
        elif direction is 'down':
            while( x != 14 and self.b.board[x + 1][y].state is not BoardPositionState.EMPTY):
                x += 1
                tiles.append(self.b.board[x][y].tile)
        elif direction is 'left':
            while( y != 0 and self.b.board[x][y - 1].state is not BoardPositionState.EMPTY):
                y -= 1
                tiles.insert(0, self.b.board[x][y].tile)
        elif direction is 'right':
            while( y != 14 and self.b.board[x][y + 1].state is not BoardPositionState.EMPTY):
                y += 1
                tiles.append(self.b.board[x][y].tile)

        else:
            assert(false, "invalid direction passed into '_scan()'.  value should be up down left or right.")

        return tiles


    def form_words(self):
        tiles, xCoords, yCoords = zip(*self.xytiles) # unzip the tuple
        wordsAndPoints = []
        y = yCoords[0]
        x = xCoords[0]
        anchorTiles = []

        if(self.row):
            anchorTiles.extend(self._scan('left', x, y))
            anchorTiles.append(tiles[0])
            anchorTiles.extend(self._scan('right', x, y))

            for y in yCoords:
                tempTiles = []
                tempTiles.extend(self._scan('up', x, y))
                tempTiles.append(self.b.board[x][y].tile)
                tempTiles.extend(self._scan('down', x, y))

                if(len(tempTiles) > 1):
                    word = self.tiles_to_string(tempTiles)
                    points = self.calculate_points(tempTiles, [self.b.board[x][y].multiplier], [self.b.board[x][y].tile])
                    wordsAndPoints.append((word, points, 0))
        else:
            anchorTiles.extend(self._scan('up', x, y))
            anchorTiles.append(tiles[0])
            anchorTiles.extend(self._scan('down', x, y))

            for x in xCoords:
                tempTiles = []
                tempTiles.extend(self._scan('left', x, y))
                tempTiles.append(self.b.board[x][y].tile)
                tempTiles.extend(self._scan('right', x, y))

                if(len(tempTiles) > 1):
                    word = self.tiles_to_string(tempTiles)
                    points = self.calculate_points(tempTiles, [self.b.board[x][y].multiplier], [self.b.board[x][y].tile])
                    wordsAndPoints.append((word, points, 0))

        word = self.tiles_to_string(anchorTiles)
        points = self.calculate_points(anchorTiles, self.get_anchor_multipliers(xCoords, yCoords), tiles)
        wordsAndPoints.append((word, points, 0))

        return wordsAndPoints


    def tiles_to_string(self, tiles):
        word = ""
        for tile in tiles:
            word = word + tile.letter

        return word


    def calculate_points(self, tiles, multipliers, pendingTiles):
        points = 0
        multiplier = 1

        if(len(multipliers) != len(pendingTiles)):
            assert(False, "calculate_points(): pending tiles and multipliers should always have the same length")

        for tile in tiles:
            points += tile.points

        for i in xrange(len(multipliers)):
            if(multipliers[i] is Multiplier.DOUBLE_LETTER):
                points += tiles[i].points
            elif(multipliers[i] is Multiplier.TRIPLE_LETTER):
                points += tiles[i].points * 2
            elif(multipliers[i] is Multiplier.DOUBLE_WORD):
                multiplier *= 2
            elif(multipliers[i] is Multiplier.TRIPLE_WORD):
                multiplier *= 3

        points *= multiplier
        return points


    def get_anchor_multipliers(self, xCoords, yCoords):
        multipliers = []

        if(len(xCoords) != len(yCoords)):
            assert(False, "get_anchor_multipliers(): xCoords and yCoords should always have the same length")

        for i in xrange(len(xCoords)):
            multipliers.append(self.b.board[xCoords[i]][yCoords[i]].multiplier)

        return multipliers
