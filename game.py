from enum import Multiplier, BoardPositionState
from board import Board
from manager import Manager

class Game(object):
    def __init__(self):
        self.b = new Board()
        self.manager = new Manager(self.b)
        self.player = new Player("Scott", self.b)
        self.ai = new Player("AI", self.b)
        self.tilebag = new Tilebag("setup/tileset.txt")

    def print_board(self):
        self.b.print_board()


