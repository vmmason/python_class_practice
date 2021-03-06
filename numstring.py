class NumString:
    def __init__(self, value):
        self.value = str(value)
        
    def __str__(self):
        return self.value
    
    def __int__(self):
        return int(self)
    
    def __float__(self):
        return float(self)
    
    def __add__(self, other):
        if "." in self.value:
            return float(self) + other
        return int(self) + other