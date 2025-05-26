from constants import BLACK, WHITE, BLACK_STR, WHITE_STR

class Pawn:

    def __init__(self, color="BLACK"):
        self.color=color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):

        if color in ["WHITE","BLACK"]:
            return self._color
        else:
            raise ValueError ("color is not in the board")
        
    def swapcolor(self):
        if self.color=="WHITE":
            return "WHITE"
        else:
            return "BLACK"
    
    def __repr__(self):
        return f"Pawn(color={self.color})"





    
