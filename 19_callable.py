class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of the class
times_two = Multiplier(2)

# ✅ Check if the object is callable
print(callable(times_two))  # Output: True

# ✅ Use the object like a function
result = times_two(5)       # Equivalent to times_two.__call__(5)
print(result)               # Output: 10
