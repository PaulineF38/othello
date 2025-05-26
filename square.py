from pawn import Pawn

class Square:

    def __init__(self):
        self.pawn=None
            
    def empty_square(self):                   #si la case st vide
         if self.pawn is None:
             return 
         else:
             raise ValueError ("the square is already occuped")

    def set_square(self,poins):               #si elle est vide on pose le pawn

        pass
