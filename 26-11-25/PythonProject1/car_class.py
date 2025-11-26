class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)

car1=Car("Hari","Mercedes",2.30000)
car1.display()
print()

car2=Car("Krittika","BMW",3.40000)
car2.display()
print()

car3=Car("Harish","Audi",1.10000)
car3.display()
print()