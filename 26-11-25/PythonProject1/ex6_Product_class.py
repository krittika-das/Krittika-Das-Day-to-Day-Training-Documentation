class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def count(self):
        return self.quantity*self.price

p1=Product("Wheat", 230, 2)
print("Total cost = ", p1.count())
print()
p2=Product("Maida", 111, 3)
print("Total cost = ", p2.count())
print()