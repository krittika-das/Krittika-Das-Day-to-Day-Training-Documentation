class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

e=ElectronicProduct("Laptop",1050,5)
print(e.name, e.price, e.warranty, " Years")