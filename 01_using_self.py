# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor.
#  Add a method display() that prints student details.

class Student ():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"My name is {self.name} and my last exam marks is {self.marks}")

st = Student("Parvez Ahmed", 95)
st.display()