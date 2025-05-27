from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    def __init__(self,adjacent_squares=[]): 
        """_summary_
        init the empyty list and put the square in this list 
        content of square : None or Pawn
        Args:
            adjacent_squares (list, optional): _description_. Defaults to [].
        """
        self.content=None                        
        self.adjacent_squares=adjacent_squares  


    def empty_square(self):  
        """
        def of the empty square

        Returns: None
        """                    
        return self.content is None
        
    def fill_square(self,pawn): 
        """
        fill the square if is empty
        Args:
            pawn (Pawn): input

        Raises:
            ValueError: the square is already occuped
        """                 
        if self.empty_square():
            self.content=pawn
        else:
            raise ValueError("the square is already occuped")
    

    @property                           
    def adjacent_squares(self):
        return self._adjacent_squares
    
    @adjacent_squares.setter
    def adjacent_squares(self,adjacent_squares : list)->list:
        self._adjacent_squares=adjacent_squares

    
    def add_adjacent(self,square): # possibility to add the squares in the liste 
        """_summary_
        add square in the list adjacent 
        Args:
            square (Square): create by board
        """        
        self.adjacent_squares.append(square)
    

    def __repr__(self):
        return f"Square(Square={self.content})"
    
    def __str__(self):
        if self.empty_square() :
            return  "    "
        else:
            return " " + str(self.content) + " "

    