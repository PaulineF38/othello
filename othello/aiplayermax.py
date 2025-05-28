from .aiplayer import AIPlayer
from .board import Board
from .game import Game

class AIPlayerMax(AIPlayer) :
    """ 
    Quite naive AI player that tries to max its point with a simple strategy
    """
    
    # --------------------------------------------------------------------------
    #                                                                Constructor
    # --------------------------------------------------------------------------

    def __init__(self, color: int) -> None:
        """Init a AI Player that use the Max strategy

        Args:
            color (int): Color of the pawns of the player
        """
        # Calling superclass constructor
        super().__init__(color, "AI:Maximator")

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------

    # This is an override :
    def play(self, board:Board) -> str:
        """Return the AI's move based on the given board

        Args:
            board (Board): the state of the game used to decide what to do

        Returns:
            str: move to do (ex: "C2" or QUIT_STR to rage quit ...)
        """
        # Get all possible moves
        legal_moves = board.list_legal_moves(self.color)

        # Check score for all moves
        scores = [ board.number_of_capture(self.color, i, j) for i,j in legal_moves]

        # Get the best score :
        best_score = max(scores)
        idx_best_score = scores.index(best_score)

        # Get the corresponding move
        move_str = Game.coord_to_str(*legal_moves[idx_best_score])

        # Print
        print(f"{self.name}'s move : {move_str}")

        return move_str
    