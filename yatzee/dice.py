import random

class Dice:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least two sides!")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number!")
        self.value = value or random.randint(1, sides)
        
    def __int__(self):
        return self.value
        
    def __eq__(self, other):
        return int(self) == other
    
    def __ne__(self, other):
        return not int(self) == other
    
    def __gt__(self, other):
        return int(self) > other
    
    def __lt__(self, other):
        return int(self) < other
    
    def __ge__(self, other):
        return int(self) > other or int(self) == other
    
    def __le__(self, other):
        return int(self) < other or int(self) == other
    
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return int(self) + other
    
        
class D6(Dice):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
        
class D20(Dice):
    def __init__(self, value=0):
        super().__init__(sides=20, value=value)