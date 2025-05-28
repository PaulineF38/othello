from square import Square
from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Board:
    def __init__(self, n_rows: int = 8, n_cols: int = 8):
        """ Create the board.

        Args:
            n_rows (int): number of rows
            n_cols (int): number of cols
        """  
        if n_rows < 4 or n_cols < 4 :
            raise ValueError("The Board must be at least 4x4 !")
        if 26 < n_cols :
            raise ValueError("The Board must have at max 26 columns (A to Z) !")
        if n_rows%2 ==1 or n_cols%2 == 1 :
            raise ValueError("The Board must be NxM with N and M two even numbers !")
            
        self._grid = [
            [Square() for _ in range(n_rows)]
            for _ in range(n_cols)
        ]
        
        # Define all 8 possible directions around a square (including diagonals)
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        # For each square on the board
        for i, row in enumerate(self.grid):
            for j, square in enumerate(row):
                # For each possible adjacent direction
                for k, l in directions :
                    # Check if the neighboring position is within board limits
                    if self._position_is_ok(i+k,j+l) :
                        # Add the valid neighboring square as adjacent
                        square.add_adjacent(self.grid[i+k][j+l]) 

        n_rows = len(self.grid)
        n_cols = len(self.grid[0])

        # Initialization of the board with the starting pawns
        self._grid[n_rows//2-1][n_cols//2-1].fill_square(Pawn(WHITE))
        self._grid[n_rows//2-1][n_cols//2].fill_square(Pawn(BLACK))
        self._grid[n_rows//2][n_cols//2-1].fill_square(Pawn(BLACK))
        self._grid[n_rows//2][n_cols//2].fill_square(Pawn(WHITE))

    @property
    def grid(self):
        return self._grid

    def draw_board(self) -> str: 
        """ Display the board in the terminal.

        Returns:
            str: board of the game that is send to Game.
        """    
        # First raw of the board
        display = "    " + "    ".join([ chr(ord("A")+i) for i in range(0, len(self._grid[0])) ] ) +"\n"
        display += " +----"
        #add first line of +---- +
        for i in range (len(self._grid[0])-1):
            display += "+----"
        display += "+\n"
        for i, row in enumerate(self._grid):
            # print nulber of rows
            display += f"{i+1}"
            
            for square in row:
                display += "|"
                # add "   " if empty or pawn emojy if not.
                display += str(square)
            # close the last line of the board with +----+
            display += '|\n'
            display += " +----"
            for i in range (len(self._grid[0])-1):
                display += "+----"
            display += "+\n"
        return display            
        

    def score(self) -> dict:
        """Calculate the score of each player.

        Returns:
            dict: {white : score (int), black : score (int)}
        """  
        dict_score = {}
        # Initialization score 
        dict_score["White "] = 0
        dict_score["Black "] = 0
        for i, row in enumerate(self._grid):
            for square in row:
                # If the square is not empty, check the color of the pawn and increment player's score
                if not square.empty_square() :
                    if square.content.color == WHITE :
                        dict_score["White "] += 1
                    elif square.content.color == BLACK:
                        dict_score["Black "] += 1
        return dict_score

        

    def _adjacent (self, i: int, j: int) -> bool:
        """  Check if adjacent squares are empty.

        Args:
            i (int): 1st coordinate of a squares (row)
            j (int): 2nd coordinates of a squares (column)

        Returns:
            bool: True = at least one square is not empty.
                  False = all adjacent squares are empty. 
        """ 
        
        return any( [ not square.empty_square() for square in self.grid[i][j].adjacent_squares])


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
            while self._position_is_ok(i+n*k, j+n*l) and not self.grid[i+n*k][j+n*l].empty_square() :
                pawns_in_direction.append(self.grid[i+n*k][j+n*l].content)
                n = n + 1
            # Search the first pawn of the given color to know if we can flip some pawn
            colors = [pawn.color for pawn in pawns_in_direction]
            idx = colors.index(color) if color in colors else 0
            # Complete the list of flippable pawns
            pawns += pawns_in_direction[:idx] 
        return pawns

    def _position_is_ok(self, i: int,j: int) -> bool:
        """ Check if the given position (i, j) is allowed in an othello board

        Args:
            i (int) : 1st coordinate (row)
            j (int) : 2nd coordinates (column)
        Returns:
            bool: True = the position is ok
                  False = the position is not ok
        """
        return 0 <= i and i < len(self._grid) and 0 <= j and j < len(self._grid[0])
    
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
        return self.grid[i][j].empty_square() and self._adjacent(i, j) and len(self._capture(color, i, j))>0 

    def list_legal_moves(self, color: int) -> list:
        """
        Give all the possible moves for the given color

        Args:
            color (int) : The color of the pawn (BLACK or WHITE).

        Returns:
            list: list of all the position possible given as tuple (i,j), if nothing is possible return empty list.   
        """
        legal_move = [] 
        for i in range(0, len(self.grid)) :
            for j in range(0, len(self.grid[i])) :
                if self.is_legal_move(color, i, j):
                    legal_move.append((i,j))
        return legal_move

    def make_move(self, color, position : tuple):
        
        """Return the board with the new pawn if move is possible.

        Args:
            color (int): The color of the pawn (BLACK or WHITE).
            position (tuple): Coordinates (i, j).
        
        Returns:
            bool: True = the move has been done
                  False = the move hasn't been done
        """    
        # converte tuple in i,j
        i, j = position

        # check if the player give a legal position to put his pawn
        if self.is_legal_move(color, i, j):
            # Place the pawn on the square
            self.grid[i][j].fill_square(Pawn(color))
            # flip pawn which need to be fliped
            list_pawn = self._capture(color, i, j)
            for pawn in list_pawn :
                pawn.flip()          
            return True
        else:
            return False



if __name__=='__main__':
    board1 = Board()
    print(board1.draw_board())
    

