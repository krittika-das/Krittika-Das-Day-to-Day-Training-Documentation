class Programmer:
    def __init__(self, name, age, ty):
        self.name = name
        self.age = age
        self.ty = ty
    def display(self):
        print(self.name)
        print(self.age)
        print(self.ty)

class Statistician:
    def __init__(self, maths):
        self.maths = maths
    def show(self):
        print("Can do: ", self.maths)

class DataSc(Programmer, Statistician):
    def __init__(self, name, age, ty, maths, stat):
        Programmer.__init__(self, name, age, ty)
        Statistician.__init__(self, maths)
        self.stat = stat
    def trial(self):
        print("A data scientist is both a programmer and a statistian and do ", self.maths, ",", self.stat)


x=DataSc("Krittika", 22, "ML", "maths", "statistics")
x.show()
x.display()
x.trial()