class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l + self.b)

x=Rectangle(23,12)
print(x.area())
print(x.perimeter())

