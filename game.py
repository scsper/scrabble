from enum import Multiplier, BoardPositionState
from board import Board
from manager import Manager
from player import Player
from tilebag import Tilebag

class Game(object):
    def __init__(self):
        self.b = Board()
        self.manager = Manager(self.b)
        self.player = Player("Scott", self.b)
        self.ai = Player("AI", self.b)
        self.tilebag = Tilebag("setup/tileset.txt")

    def print_board(self):
        self.b.print_board()


