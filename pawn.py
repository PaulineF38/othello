from constants import BLACK, WHITE, BLACK_STR, WHITE_STR

class Pawn:

    def __init__(self, color=BLACK):
        self.color=color
        """_summary_
        init th color of the pawn
        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """        
    @property
    def color(self):
        """_summary_
        acess getter color
        Returns:
            _type_: _description_
        """        
        return self._color
    
    @color.setter
    
    def color(self, color):
        """_summary_
        the getter of the attribut color
        Args:
            color (int): input 

        Raises:
            ValueError: color is not valid"
        """        
        if color in [WHITE, BLACK]:
            self._color = color
        else:
            raise ValueError ("color is not valid")
        
    def flip(self) -> None :
        """
        flip the pawn by the color
        """          
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