# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Emplyee():
    def __init__(self, name, salary,ssn):
        self.name = name
        self._salary =salary
        self.__ssn =ssn

emp = Emplyee("Ali", 5000, "123-45")
print("public ", emp.name)
print("Protected: ", emp._salary)
try:
    print("private", emp.__ssn)
except AttributeError as  e:
    print("can't access directly" ,e)
print("by force", emp._Emplyee__ssn) # not recommended.....❌❌