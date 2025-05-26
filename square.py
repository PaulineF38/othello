from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pawn=None                 # par défaut
        list_adjacent=[]

    def set_square(self,poins):              #si elle est vide on pose le poins 
        self.poins=poins
        if self.empty_square():
            return self.pawn=poins 
        else:
            return f"the square is already occuped"