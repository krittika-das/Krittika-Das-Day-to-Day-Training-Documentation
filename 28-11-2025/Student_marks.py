class Student:
    def __init__(self,  a, b ,c):
        self.a=a
        self.b=b
        self.c=c
    def total(self):
        return self.a+self.b+self.c
    def percent(self):
        return (self.total()/300) * 100

s=Student(78,89, 94)

print(s.percent())