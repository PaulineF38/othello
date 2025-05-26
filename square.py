from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pawn=None                # par défaut on considère que la case est vide
        list_adjacent=[]
    
    def empty_square(self):          # le cas si ma case est vide
        if self.pawn is None:
            return self.pawn
        
    def set_square(self,poins):              #pour poser : si elle est vide on pose le poins 
        self.poins=poins
        if self.empty_square():
            self.pawn=poins 
        else:
            return f"the square is already occuped"
        
    def __repr__(self):
        return f"Square(Square={self.pawn})"
    