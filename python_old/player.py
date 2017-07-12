from tile import Tile
from board import Board
import sys

class Player(object):
    def __init__(self, name, board):
        self.name = name
        self.points = 0
        self.rack = []
        self.board = board # store a reference to the game board

    def place(self, tile, x, y):
        if(self.board.place_tile(tile, x, y)):
            try:
                self.rack.remove(tile)
            except:
                e = sys.exc_info()[0]
                print e


    def retrieve_tile(self, x, y):
        retrieved = self.board.retrieve_tile(x, y)

        if(retrieved):
            self.rack.append(retrieved)


    def retrieve_all(self):
        self.rack.extend(self.board.retrieve_all())


    # def pass_turn(self):
    #     # hand over the turn
    #     # make sure there is nothing on the board
    #     # yada yada

    # def play_turn(self):
    #     # go to the game manager, yada yada
    #     # get tiles back

    # def swap_tiles(self, tiles):
    #     # check for tiles on rack
    #     # swap them
    #     # get the tiles back




