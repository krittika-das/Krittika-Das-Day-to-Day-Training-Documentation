class Student:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def total(self):
        return self.A + self.B + self.C
    def percentage(self):
        return (self.total()/ 300) * 100
    def grade(self):
        if self.percentage() > 90:
            return "A"
        elif self.percentage() > 80:
            return "B"
        elif self.percentage() > 70:
            return "C"
        else:
            return "D"

x=Student(94, 75, 82)
print("Your grade is ", x.grade())
