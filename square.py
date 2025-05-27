from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    """this class takes an empyty list and content of thes square
    """
    def __init__(self,adjacent_squares=[]): # initialise with the empty list of adjacent squares

        self.content=None                        
        self.adjacent_squares=adjacent_squares  


    def empty_square(self):                 # the function of empty square
        return self.content is None
        
    def fill_square(self,pawn):          #if the square is empty we fill it with pawn
        if self.empty_square():
            self.content=pawn
        else:
            raise ValueError("the square is already occuped")
    

    @property                           
    def adjacent_squares(self):
        return self._adjacent_squares
    
    @adjacent_squares.setter

    def adjacent_squares(self,adjacent_squares):
        self._adjacent_squares=adjacent_squares

    
    def add_adjacent(self,square): # possibility to add the squares in the liste 

        self.adjacent_squares.append(square)
        
    def __repr__(self):
        return f"Square(Square={self.content})"
    

    def __str__(self):
        if self.empty_square():
            return  "    "
        else:
            return self.content
    