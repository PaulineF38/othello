from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR, MIN_ROWS, MIN_COLS, MAX_ROWS, MAX_COLS

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

    def play(self, info: str) -> str:
        """Display something to the player and ask him what to do

        !!!! THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES !!!!

        Args:
            info (str): info to display to the player

        Returns:
            str: input given by the user
        """
        raise NotImplementedError("THIS METHOD MUST BE OVERRIDEN IN THE SUBCLASSES")
    
    @staticmethod
    def ask_rows() -> str:
        """ask number of rows to players

        Returns:
            str: number of rows
        """
        return int(input("Number of rows: "))
    
    @staticmethod
    def ask_cols() -> str:
        """ask number of cols to players

        Returns:
            str: number of cols
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
