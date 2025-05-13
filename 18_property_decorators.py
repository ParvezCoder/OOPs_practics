class Product:
    def __init__(self, price):
        self._price = price  # private attribute
    @property
    def price(self):
        print("Getting price...")
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price...")
        self._price = value
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
# Example usage
product = Product(100)
# Get price
print(product.price)  # Output: Getting price... 100
# Set price
product.price = 150   # Output: Setting price...
# Get updated price
print(product.price)  # Output: Getting price... 150
# Delete price
del product.price     # Output: Deleting price...