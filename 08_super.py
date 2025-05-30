# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name.
#  Inherit a class Teacher from it, add a subject field, and use super() 
#  to call the base class constructor.

class Person():
    def __init__(self, name):
        self.name = name

class Teacher (Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"""name taken from Person class which is {self.name} and sub
from Teacher class {self.subject} """)
        
tee = Teacher("Ali", "math")