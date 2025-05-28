from .player import Player
from .board import Board

class AI(Player) : 
    """ 
    Base Class for AI Players
    """
    
    # --------------------------------------------------------------------------
    #                                                                Constructor
    # --------------------------------------------------------------------------

    def __init__(self, color: int, name: str) -> None:
        """Init a generic AI Player

        Args:
            color (int): Color of the pawns of the player
            name (str) : Name of the Player
        """
        # Calling superclass constructor
        super().__init__(color, name)

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------

    def play(self, board:Board) -> str:
        """Return the AI's move based on the given board

        !!!! THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES !!!!

        Args:
            board (Board): the state of the game used to decide what to do

        Returns:
            str: move to do (ex: "C2" or QUIT_STR to rage quit ...)
        """
        raise NotImplementedError("THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES")
    
