class Board:
    def __init__(self,grid):
        self._grid = grid
    
    @property
    def grid(self):
        return self._grid

    def draw_board() -> str: 
        """ Display the board in the terminal.

        Returns:
            str: board of the game that is send to Game.
        """                
        pass

    def score() -> dict:
        """Calculate the score of each player.

        Returns:
            dict: {white : score (int), black : score (int)}
        """        
        pass

    def get_square(position : tuple) -> square:
        """
        Get the square at the given coordinates.

        Args:
            position (tuple): Coordinates (i, j) on the board.

        Returns:
            Square: Instance of the Square class at the specified position.
        """

        pass

    def adjacent (self, position : tuple) -> bool:
        """  Check if adjacent squares are empty.

        Args:
            position (tuple): (i,j), coordinates of a squares

        Returns:
            bool: True = at least one square is not empty.
                  False = all adjacent squares are empty. 
        """ 

        pass

    def capture (self, position: tuple) -> tuple:
        """
        Find all the positions where pawns will be flipped.

        Args:
            position (tuple): (i, j), coordinates of a square.

        Returns:
            tuple: (bool, list): 
                - bool: True if at least one pawn can be flipped, False otherwise.
                - list: List of coordinates [(i1, j1), (i2, j2), ...] of pawns to flip.
        """     

        pass

    def legal_move(self, color : int , position : tuple) -> list:
        """
        Check if placing a pawn of the given color at the specified position is a legal move.

        Args:
            color (int): The color of the pawn (0 for black, 1 for white).
            position (tuple): Coordinates (i, j) on the board where the pawn is to be placed.

        Returns:
            list: list of the position possible, if nothing is possible return empty list.   
        """    
        pass

