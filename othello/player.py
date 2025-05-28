from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR

class Player() : 
    """ 
    A Player defined by its name and the color of its pawns
    """
    
    # --------------------------------------------------------------------------
    #                                                                Constructor
    # --------------------------------------------------------------------------

    def __init__(self, color: int, name: str) -> None:
        """Init a Player

        Args:
            color (int): Color of the pawns of the player
            name (str) : Name of the Player
        """
        # Set color :
        if color not in [BLACK, WHITE]:
            raise TypeError(f"Color must be either color={BLACK} ({BLACK_STR}) or color={WHITE} ({WHITE_STR}) !")
        self._color = color
        # Set name :
        self.name = name

    # --------------------------------------------------------------------------
    #                                                                 Properties
    # --------------------------------------------------------------------------

    # Color --------------------------------------------------------------------
    @property # getter
    def color(self) -> int:
        """Color played by the player"""
        return self._color

    @color.setter
    def color(self, color: int) -> None:
        raise Exception("You are not able to edit the property : color !")

    @color.deleter
    def color(self) -> None:
        raise Exception("You are not able to delete the property : color !")
    
    # Name --------------------------------------------------------------------
    @property # getter
    def name(self) -> str:
        """Name of the player"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        try :
            name = str(name) 
        except :    
            raise TypeError(f"Name must be a string (or convertible to a string)!")
        self._name = name

    @name.deleter
    def name(self) -> None:
        raise Exception("You are not able to delete the property : name !")
