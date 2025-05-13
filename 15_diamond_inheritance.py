class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("Bn")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Diamond Inheritance
    def show(self):
        print("DD")

# Create an object of class D
d = D()
d.show()  # Which show() method will be called?

# Print the Method Resolution Order
print("MRO:", D.__mro__)
