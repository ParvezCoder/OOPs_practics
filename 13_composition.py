class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started."

# Car class that uses Engine via composition
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Engine object passed to Car

    def start_car(self):
        print(f"{self.brand} car is starting...")
        print(self.engine.start())  # Accessing Engine method via Car

my_engine = Engine(200)  # Create Engine object
my_car = Car("Toyota", my_engine)  # Pass Engine object to Car
my_car.start_car()  # Start the car
