class Pawn:

    def __init__(self, color="black"):
        self.color=color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):

        if color in ["white","black"]:
            return self.__color
        else:
            raise ValueError ("color is not in the board")
        
    def swapcolor(self):
        if self.color=="white":
            return 1
        else:
            return 0
    
    def __repr__(self):
        return f"Pawn(color={self.color})"





    
