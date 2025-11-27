class Property:
    def __init__(self, location, acres):
        self.location = location
        self.acres = acres
    def display(self):
        print(self.location, self.acres)

class Building(Property):
    def __init__(self, location, acres, type):
        super().__init__(location, acres)
        self.type = type
    def use(self):
        print("This is a ", self.type)

class Apartment(Building):
    def __init__(self, location, acres, type, wings, blocks):
        super().__init__(location, acres, type)
        self.wings = wings
        self.blocks = blocks
    def isswimming(self):
        if(self.wings >4 and self.blocks >3):
            return True
        return False

x=Apartment("Barasat", 29, "Flat", 5, 2)
x.display()
x.use()
if x.isswimming():
    print("Swimming Pool Access approved")
else:
    print("Swimming Pool Access not approved")