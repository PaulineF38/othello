#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Author : Xavier BEDNAREK

from constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR

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
        # Set color :
        if color not in [BLACK, WHITE]:
            raise TypeError(f"Color must be either color={BLACK} ({BLACK_STR}) or color={WHITE} ({WHITE_STR}) !")
        self._color = color
        # Set name :
        self.name = Player.ask_name()
        # Display welcome message
        print("Welcome " + self.name + " !", end=" ")
        if self.color == BLACK :
            print("You play black pawns : " + BLACK_STR +" !", end=" ")
        if self.color == WHITE :
            print("You play white pawns : " + WHITE_STR +" !", end=" ")
        print("Good luck !")
        print("")

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

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------

    @staticmethod
    def ask_name() -> str:
        """Ask the user to give his name


        Returns:
            str: name chosen by the player
        """
        return input("Choose a name : ")

    def play(self, info: str) -> str:
        """Display something to the player and ask him what to do

        Args:
            info (str): info to display to the player

        Returns:
            str: input given by the user
        """
        try :
            answer = input(info)
        except KeyboardInterrupt :
            answer = QUIT_STR
        return answer

if __name__=='__main__':
    
    # Test player init :
    p_black = Player(BLACK)
    p_white = Player(WHITE)