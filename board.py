from square import Square
import constants

class Board:
    def __init__(self,grid):
        self._grid = grid
        self.grid = [
            [Square() for _ in range(8)]
            for _ in range(8)
        ]

        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                Square.list_voisin = i,j # a changer avec le nom de que Nouhaila donnera!


        self.grid[3][3].pawn.color = constants.WHITE
        self.grid[3][4].pawn.color = constants.BLACK
        self.grid[4][3].pawn.color = constants.BLACK
        self.grid[4][4].pawn.color = constants.WHITE


    
    @property
    def grid(self):
        return self._grid

    def draw_board(self) -> str: 
        """ Display the board in the terminal.

        Returns:
            str: board of the game that is send to Game.
        """    
        display = "    A    B    C    D    E    F    G    H\n"
        display += " +----"
        for i in range (7):
            display += "+----"
        display += "+\n"
        for i, row in enumerate(self.grid):
            display += f"{i+1}"
            
            for square in row:
                display += "|"
                if square.pawn.color == constants.WHITE:
                    display += " " + constants.WHITE_STR + " "
                elif square.pawn.color == constants.BLACK:
                    display += " " + constants.BLACK_STR + " "
                else:
                    display += "    "
            display += '|\n'
            display += " +----"
            for i in range (7):
                display += "+----"
            display += "+\n"
        return display            
        

    def score() -> dict:
        """Calculate the score of each player.

        Returns:
            dict: {white : score (int), black : score (int)}
        """        
        pass

    def get_square(position : tuple) -> Square:
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

        i, j = position  
        directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0), (1, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                neighbor_square = self.grid[ni][nj]
                if neighbor_square.pawn is not None:
                    return True  
        
        return False  

    def capture (self, position: tuple) -> list:
        """
        Find all the positions where pawns will be flipped.

        Args:
            position (tuple): (i, j), coordinates of a square.

        Returns:
            list: List of coordinates [pawn, pawn, ...] of pawns to flip.
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
        i, j = position
        square = self.grid[i][j]

        if square.pawn is not None:
            return []


