class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(self.brand, self.model, self.year)
    def age(self):
        return 2025 - self.year

class Car(Vehicle):
    def __init__(self, brand, model, year, warranty_period):
        super().__init__(brand, model, year)
        self.warranty_period = warranty_period
    def check_warranty(self):
        if self.warranty_period < self.age():
            print("Warranty Present")
        else:
            print("Out of Warranty")

x=Car("Toyota", "XA11", 2011, 15)
x.display()
print("Current Age: ", x.age())
x.check_warranty()
