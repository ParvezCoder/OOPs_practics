# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that 
# returns the sum. No class or instance variables should be used.
class MathUtil():

    @staticmethod
    def add(a,b):
        return a+b
    
result = MathUtil.add(2,6)
print(result)