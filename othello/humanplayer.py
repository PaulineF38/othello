from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR
from .player import Player
from .board import Board

class HumanPlayer(Player) : 
    """ 
    A Human Player defined by its name and the color of its pawns
    """
    
    # --------------------------------------------------------------------------
    #                                                                Constructor
    # --------------------------------------------------------------------------

    def __init__(self, color: int) -> None:
        """Init a Human Player by asking its name to the user

        Args:
            color (int): Color of the pawns of the player
        """
        # Calling superclass constructor
        super().__init__(color, HumanPlayer.ask_name()) 
        # Display welcome message
        print("Welcome " + self.name + " !", end=" ")
        if self.color == BLACK :
            print("You play black pawns : " + BLACK_STR +" !", end=" ")
        if self.color == WHITE :
            print("You play white pawns : " + WHITE_STR +" !", end=" ")
        print("Good luck !")
        print("")

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

    # This is an override
    def play(self, prompt:str, board:Board) -> str:
        """Display something to the player and ask him what to do

        Args:
            prompt (str): info to display to the player
            board (Board): the state of the game used to decide what to do ---> NOT USED HERE

        Returns:
            str: input given by the user
        """
        try :
            answer = input(prompt)
        except KeyboardInterrupt :
            answer = QUIT_STR
        return answer
