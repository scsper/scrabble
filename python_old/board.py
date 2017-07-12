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


    def place_tile(self, tile, row, col):
        if(self.board[row][col].state == BoardPositionState.EMPTY):
            self.board[row][col].state = BoardPositionState.PENDING
            self.board[row][col].tile = tile
            return True
        else:
            return False


    def retrieve_tile(self, row, col):
        retrieved = self.board[row][col].tile

        if(retrieved and self.board[row][col].state is BoardPositionState.PENDING):
            self.board[row][col].state = BoardPositionState.EMPTY
            self.board[row][col].tile = None
        else:
            return False

        return retrieved


    def retrieve_all(self):
        tiles = []
        # scan the board for pending
        for row in xrange(15):
            for col in xrange(15):
                if(self.board[row][col].state == BoardPositionState.PENDING):
                    tiles.append(self.retrieve_tile(row, col))

        return tiles


    def build_board(self):
        for row in xrange(15):
            for col in xrange(15):
                self.board[row][col] = BoardPosition(self.board[row][col])

    def print_board(self):
        for row in xrange(15):
            print
            for col in xrange(15):
                print str(self.board[row][col]) + ' ',
        print
        print


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

    def __repr__(self):
        if(self.tile):
            return self.tile.letter
        else:
            return str(self.multiplier)

    # for testing purposes
    def __eq__(self, other):
        return self.state == other.state and self.name == other.name
