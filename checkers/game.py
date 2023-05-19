from .constants import RED, WHITE, BLUE
from checkers.board import Board

class Game:
    def init(self):
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def set_board(self, board):
        self.board.set_board(board)

    def get_board(self):
        return self.board