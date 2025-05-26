# -*- coding: utf8 -*-
#
# Author : Xavier BEDNAREK

from constants import BLACK, WHITE, BLACK_STR, WHITE_STR

class Player() : 
    """ 
    A Player defined by its name and the color of its pawns
    """
    
    # --------------------------------------------------------------------------
    #                                                                Constructor
    # --------------------------------------------------------------------------

    def __init__(self, color: int) -> None:
        """Init a Player by asking its name to the user

        Args:
            color (int): _description_
        """
        pass

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
        if color not in [BLACK, WHITE]:
            raise TypeError(f"Color must be either color={BLACK} ({BLACK_STR}) or color={WHITE} ({WHITE_STR}) !")
        self._color = color

    @color.deleter
    def color(self) -> None:
        raise Exception("You can not do that !")
    
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
        raise Exception("You can not do that !")

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------
    
    def play(self, info: str) -> str:
        """Display something to the player and ask him what to do

        Args:
            info (str): info to display to the player

        Returns:
            str: input given by the user
        """
        pass