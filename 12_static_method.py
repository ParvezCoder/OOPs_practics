# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method 
# celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
tem_c = 25
tem_f = TemperatureConverter.celsius_to_fahrenheit(tem_c)
print(f"{tem_c}°C is equal to {tem_f}°F")