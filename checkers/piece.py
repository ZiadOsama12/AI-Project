from .constants import RED, WHITE, GREY

class Piece:


    def init(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0

    def make_king(self):
        self.king = True

    def is_king(self):
        return self.king

    def move(self, row, col): # move some piece
        self.row = row
        self.col = col

    def repr(self):
        return str(self.color)