from .aiplayer import AIPlayer
from .board import Board
from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR
import random

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
        # Print 
        print(f"{self.name} is entering the game !", end=" ")
        if self.color == BLACK :
            print("It plays black pawns : " + BLACK_STR +" !")
        if self.color == WHITE :
            print("Its plays white pawns : " + WHITE_STR +" !")
        print("")

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------

    # This is an override :
    def play(self, prompt:str, board:Board) -> str:
        """Return the AI's move based on the given board

        Args:
            prompt (str): info to display to the player ---> NOT USED HERE
            board (Board): the state of the game used to decide what to do

        Returns:
            str: move to do (ex: "C2" or QUIT_STR to rage quit ...)
        """
        # Get all possible moves
        legal_moves = board.list_legal_moves(self.color)

        # Shuffle to add a bit of randomness when choosing the best score
        random.shuffle(legal_moves)

        # Check score for all moves
        scores = [ board.number_of_capture(self.color, i, j) for i,j in legal_moves]

        # Get the best score :
        best_score = max(scores)
        idx_best_score = scores.index(best_score)

        # If best score is zero, then rage quit !
        if best_score == 0 :
            return QUIT_STR

        # Get the corresponding move
        from .game import Game # Import here to avoid circular import !
        move_str = Game.coord_to_str(*legal_moves[idx_best_score])

        # Print
        print(f"{prompt} : {move_str} (played by {self.name})")

        return move_str
    