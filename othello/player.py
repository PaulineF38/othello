from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR, MIN_ROWS, MIN_COLS, MAX_ROWS, MAX_COLS, LIST_MODE, LIST_MODE_DESCR
from .board import Board

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

    # --------------------------------------------------------------------------
    #                                                                    Methods
    # --------------------------------------------------------------------------

    def play(self, prompt:str, board:Board) -> str:
        """Return the AI's move based on the given board

        !!!! THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES !!!!

        Args:
            prompt (str): info to display to the player
            board (Board): the state of the game used to decide what to do

        Returns:
            str: move to do (ex: "C2" or QUIT_STR to rage quit ...)
        """
        raise NotImplementedError("THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES")

    # --------------------------------------------------------------------------
    #                                                             Static Methods
    # --------------------------------------------------------------------------
    
    @staticmethod
    def ask_rows() -> int:
        """ask number of rows to players

        Returns:
            int: number of rows
        """
        return int(input("Number of rows: "))
    
    @staticmethod
    def ask_cols() -> int:
        """ask number of cols to players

        Returns:
            int: number of cols
        """
        return int(input("Number of cols: "))

    @staticmethod
    def ask_board() -> tuple:
        """Asks the players on which board they want to play

        Returns:
            tuple: number of rows, number of cols
        """
        print("Choose your board!\n(min 4x4, max 26 columns and 100 rows, and only even numbers)")
        n_rows = Player.ask_rows()
        n_cols = Player.ask_cols()
        while n_rows < MIN_ROWS or n_cols < MIN_COLS or MAX_COLS < n_cols or n_rows%2 ==1 or n_cols%2 == 1:
            if n_rows < MIN_ROWS or n_cols < MIN_COLS:
                print("------\nYour Board is invalid\nThe Board must be at least 4x4 !")
                print("Choose a valid board!\n(min 4x4, max 26 columns and 100 rows, and only even numbers)")
                n_rows = Player.ask_rows()
                n_cols = Player.ask_cols()
            elif MAX_COLS < n_cols or MAX_ROWS < n_rows:
                print("------\nYour Board is invalid\nThe Board must have at max 26 columns (A to Z) and 100 rows !")
                print("Choose a valid board!\n(min 4x4, max 26 columns and 100 rows, and only even numbers)")
                n_rows = Player.ask_rows()
                n_cols = Player.ask_cols()
            else: 
                print("------\nYour Board is invalid\nThe Board must be NxM with N and M two even numbers !")
                print("Choose a valid board!\n(min 4x4, max 26 columns and 100 rows, and only even numbers)")
                n_rows = Player.ask_rows()
                n_cols = Player.ask_cols()
        return n_rows, n_cols
    
    @staticmethod
    def ask_mode() -> int:
        """Asks the players on which mode they want to play

        Returns:
            int: the mode given by a constant see constants.py, MODE_*
        """
        print("Please choose how you want to play the Othello !")
        for mode in LIST_MODE :
            print(f"{mode+1} : {LIST_MODE_DESCR[mode]} -")

        answer = ""
        while not answer.isdigit() or (int(answer)-1) not in LIST_MODE :
            answer = input(f"Your choice ? (Number between 1 and {len(LIST_MODE)})")
        
        return int(answer)-1
    
