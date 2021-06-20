#Object Oriented Programming Practice from Corey Schafer's YT Videos

#A class is a blueprint for creating instances
#When creating the constructor class, always name the instance 'self'.
#full_name is a method of the Employee class that can be run on any instance of the Employee() class
#All methods require self as the argument
class Employee:
    def __init__(self, first, last, astrology):
        self.first = first
        self.last = last
        self.astrology = astrology
        self.email = first + '.' + last +"@gmail.com"
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Veron", "Mason", "Sagittarius")
emp_2 = Employee("Tori", "Edwardson", "Aquarius")
#Each of these variables are instances of the Employee() class with unique locations in memory.

print(emp_1.email)
print(emp_2.email)
#These print() functions access attributes of the Employee() class
#Attributes do not need () to be called

print(emp_1.full_name())
print(emp_2.full_name())
#This print() function calls the full_name() method/function of the Employee() class
#Unlike attributes, methods need () to be called
#This function is the same as print(Employee.full_name(emp_1))

