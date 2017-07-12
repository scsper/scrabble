class Tile(object):
    def __init__(self, letter, points):
        self.letter = letter
        self.points = points

    def __eq__(self, other):
        return self.letter == other.letter and self.points == other.points

    def __str__(self):
        string = self.letter + " " + str(self.points)
        return string
