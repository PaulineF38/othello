from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    def __init__(self,adjacent_squares):
        self.content=None                # par défaut on considère que la case est vide
        self.adjacent_squares=[]


    def empty_square(self):                 # le cas si ma case est vide
        return self.content is None
        
    def fill_square(self,pawn): #pour poser : si elle est vide on pose le poins 
        if self.empty_square():
            self.content=pawn
        else:
            raise ValueError("the square is already occuped")
    

    @property                           
    def adjacent_square(self):
        return self._adjacent_square
    
    def add_adjacent(self,square): # add les squares dans la liste adjacents

        self.adjacent_squares.append(square)
        
    def __repr__(self):
        return f"Square(Square={self.content})"
    

    def __str__(self):
        if self.empty_square():
            return self.content
        else:
            return "    "
    