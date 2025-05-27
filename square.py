from constants import BLACK, WHITE, BLACK_STR, WHITE_STR
from pawn import Pawn

class Square:

    def __init__(self,adjacent_squares=[]): # initialise with the empty list of adjacent squares
        """_summary_
        init the empyty list and put the square in this list 
        content of square : None or Pawn
        Args:
            adjacent_squares (list, optional): _description_. Defaults to [].
        """
        self.content=None                        
        self.adjacent_squares=adjacent_squares  


    def empty_square(self):  
        """_summary_
        def of the empaty square
        Returns:
            _type_: _description_
        """                    
        return self.content is None
        
    def fill_square(self,pawn): 
        """_summary_

        Args:
            pawn (Pawn): _description_

        Raises:
            ValueError: _description_
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
        adjacent_squares=adjacent_squares

    
    def add_adjacent(self,square): # possibility to add the squares in the liste 
        """_summary_
        add square in the list adjacent 
        Args:
            square (_type_): _description_
        """        
        self.adjacent_squares.append(square)
        
    def __repr__(self):
        
        return f"Square(Square={self.content})"
    
    def __str__(self):
            
        if self.empty_square() :
            return  "    "
        else:
            return " " + str(self.content) + " "

    