#OOP Tutorial 3: Classmethods and staticmethods practice from Corey Schafer

class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, astrology, pay):
        self.first = first
        self.last = last
        self.astrology = astrology
        self.pay = pay
        self.email = first + '.' + last +"@gmail.com"
        
        Employee.number_of_employees += 1
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, astrology, pay = emp_str.split('-')
        return cls(first, last, pay)
        #We have made an alternative constructor by applying this classmethod
        #This classmethod will make objects from the strings passed to it

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee("Veron", "Mason", "Sagittarius", 500)
emp_2 = Employee("Tori", "Edwardson", "Aquarius", 800)

emp_str_1 = ("John-Doe-Libra-700")
emp_str_2 = ("Evelyn-Beard-Aquarius-750")
emp_str_3 = ("KJ-Fischbach-Leo-600")

new_emp_1 = Employee.from_string(emp_str_1)