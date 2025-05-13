# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet method to the class
    return cls

# Apply the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance and call greet()
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!
