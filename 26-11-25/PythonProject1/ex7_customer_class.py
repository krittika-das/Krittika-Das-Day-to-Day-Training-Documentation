class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age=age
        self.city=city
    def eligible(self):
        if self.age>25:
            return True
        else:
            return False

x=Customer("Ronald Dump", 60, "Washington")
if x.eligible():
    print(x.name, " is eligible")
else:
    print(x.name, " is not eligible")