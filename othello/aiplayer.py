from .player import Player

class AIPlayer(Player) : 
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
    
