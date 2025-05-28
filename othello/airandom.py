from .player import Player
from .board import Board
from .aiplayer import AIPlayer
import random

class AIRandom(AIPlayer):
    """AI that plays by choosing a random move
    """

    def __init__(self, color: int):
        """Init the AIRandom
        """
        super().__init__(color, "Randomitor")

    def play(self, prompt:str, board:Board) -> str:
        """Returns the AI move based on the board state

        Args:
            board (Board): state of the board

        Returns:
            str: move in str (ex: 'C4')
        """
        from .game import Game
        move_str = random.choice([Game.coord_to_str(*coords) for coords in board.list_legal_moves(self.color)])
        print(f"{prompt} : {move_str} (played by {self.name})")
        return move_str