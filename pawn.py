from constants import BLACK, WHITE, BLACK_STR, WHITE_STR

class Pawn:

    def __init__(self, color=BLACK):
        self.color=color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if color in [WHITE, BLACK]:
            self._color = color
        else:
            raise ValueError ("color is not in the board")
        
    def flip(self) -> None :
        """Flip the Pawn"""

        if self.color==WHITE:
            self.color=BLACK
        else:
            self.color=WHITE
    
    def __repr__(self):
        return f"Pawn(color={self.color})"
    
    def __str__(self):
        if self.color == BLACK :
            return BLACK_STR
        else :
            return WHITE_STR
    
if __name__=='__main__':

    print("----")
    # Test PAWN init :
    p_black = Pawn(BLACK)
    print("Black pawn : " + str(p_black))
    p_white = Pawn(WHITE)
    print("White pawn : " + str(p_white))
    print("----")

    # Test flip
    pawn = Pawn(WHITE)
    print("Before flip : " + str(pawn))
    pawn.flip()
    print("After flip : " + str(pawn))
    print("----")