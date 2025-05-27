from square import Square
from constants import BLACK, WHITE, BLACK_STR, WHITE_STR

class Board:
    def __init__(self,grid):
        self._grid = [
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

    def _adjacent (self, i: int, j: int) -> bool:
        """  Check if adjacent squares are empty.

        Args:
            i (int): 1st coordinate of a squares (row)
            j (int): 2nd coordinates of a squares (column)

        Returns:
            bool: True = at least one square is not empty.
                  False = all adjacent squares are empty. 
        """ 
        
        return any( [ not square.isempty() for square in self.grid[i][j].adjacent_squares])


    def _capture (self, color: int, i: int, j: int) -> list:
        """
        Find all the pawns that should be flipped if any when adding a new pawn and the square.

        Args:
            color (int) : The color of the pawn (BLACK or WHITE).
            i (int)     : 1st coordinate of the square (row) where the new pawn try to be put on.
            j (int)     : 2nd coordinates of the square (column) where the new pawn try to be put on.
            
        Returns:
            list: List of pawns [pawn, pawn, ...] to flip (if any)
        """     
        # Check all directions from i, j square to see if there is any pawn to flip
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        pawns = []
        for k, l in directions :
            n = 1
            # Get all pawn in the current explored direction
            pawns_in_direction = []
            # While the position exists and the square contains a pawn  :
            while Board._position_is_ok(i+n*k, i+n*j) and not self.grid[i+n*k][j+n*l].empty_square() :
                pawns_in_direction.append(self.grid[i+n*k][j+n*l].pawn)
                n = n + 1
            # Search the first pawn of the given color to know if we can flip some pawn
            colors = [pawn.color for pawn in pawns_in_direction]
            idx = colors.index(color) if color in colors else 0
            # Complete the list of flippable pawns
            pawns += pawns_in_direction[:idx] 
        return pawns

    @staticmethod
    def _position_is_ok(i: int,j: int) -> bool:
        """ Check if the given position (i, j) is allowed in an othello board

        Args:
            i (int) : 1st coordinate (row)
            j (int) : 2nd coordinates (column)
        Returns:
            bool: True = the position is ok
                  False = the position is not ok
        """
        return 0 <= i and i < 8 and 0 <= j and j < 8
    
    def is_legal_move(self, color: int, i: int, j:int) -> bool:
        """
        Check if putting a pawn of the given color at the given location (i, j) is legal or not

        Args:
            color (int) : The color of the pawn (BLACK or WHITE).
            i (int) : 1st coordinate (row)
            j (int) : 2nd coordinates (column)

        Returns:
            bool: True = the move is legal
                  False = the move is not legal
        """
        return self.grid[i][j].empty_square and self._adjacent(i, j) and len(self._capture(color, i, j))>0 


    def list_legal_moves(self, color: int) -> list:
        """
        Give all the possible moves for the given color

        Args:
            color (int) : The color of the pawn (BLACK or WHITE).

        Returns:
            list: list of all the position possible given as tuple (i,j), if nothing is possible return empty list.   
        """
        legal_move = [] 
        for i in range(0, 8) :
            for j in range(0, 8) :
                if self.is_legal_move(color, i, j):
                    legal_move.append((i,j))
        return legal_move
        
