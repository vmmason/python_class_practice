import random

class Dice:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least two sides!")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number!")
        
        self.value = value or random.randint(1, sides)
        
        
class D6(Dice):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
        
class D20(Dice):
    def __init__(self, value=0):
        super().__init__(sides=20, value=value)