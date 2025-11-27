class Device:
    def __init__(self, type, store_name):
        self.type = type
        self.store_name = store_name
    def display(self):
        print("Type: ", self.type)
        print("Type: ", self.store_name)

class Computer(Device):
    def __init__(self, type, store_name, model):
        super().__init__(type, store_name)
        self.model = model
    def show(self):
        print("Model is: ", self.model)

class Laptop(Computer):
    def __init__(self, type, store_name, model, charger):
        super().__init__(type, store_name, model)
        self.charger = charger
    def charge(self):
        print("Charging: ", self.charger)

x=Laptop("laptop", "X", "HP", "B12")
x.display()
x.show()
x.charge()

