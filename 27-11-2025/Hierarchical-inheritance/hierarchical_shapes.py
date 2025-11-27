class Shapes:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter


class Square(Shapes):
    def __init__(self, area, perimeter, side):
        super().__init__(area, perimeter)
        self.side = side
    def display_square(self):
        print("Side = ", self.side)
        print("Area = ", self.area)


class Rectangle(Shapes):
    def __init__(self, area, perimeter, length, breadth):
        super().__init__(area, perimeter)
        self.length = length
        self.breadth = breadth
    def display_rectangle(self):
        print("Length = ", self.length)
        print("Breadth = ", self.breadth)
        print("Area = ", self.area)

x=Rectangle(2,3,4,5)
x.display_rectangle()

y=Square(4,5,6)
y.display_square()
