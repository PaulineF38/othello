from board import Board
from player import Player

class Game:

    def __init__(self):
        self.player1 = Player("black")
        self.player2 = Player("white")
        self.board = Board()

    def run(self):
        pass

    def str_to_coord(self):
        pass

    def flip_list(self):
        pass

    def possible_move(self):
        pass

    def game_end(self):
        pass
