from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR
from .player import Player

class Human(Player) : 
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
        super().__init__(color, Human.ask_name()) 
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

    # This is an override :
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
