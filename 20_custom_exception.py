# Step 1: Create a custom exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Must be at least 18.")

# Step 2: Function that uses the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid for registration.")

# Step 3: Use try...except to handle it
try:
    check_age(21)
except InvalidAgeError as e:
    print(f"Error caught: {e}")
