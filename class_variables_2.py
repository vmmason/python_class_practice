#OOP Tutorial 2: Class Variables practice from Corey Schafer

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
        #Using the class name does not allow the value to be overriden by subclasses
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #Using self.raise_amount allows any subclass to override the raise_amount constant

emp_1 = Employee("Veron", "Mason", "Sagittarius", 500)
emp_2 = Employee("Tori", "Edwardson", "Aquarius", 800)

emp_1.raise_amount = 1.05
#Created the raise_amount attribute within the emp_1 instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)