class calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        if self.a > self.b:
            return self.a - self.b
        else:
            return self.a - self.b
    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("Division by zero is not possible.")
            return 0
    def mul(self):
        return self.a * self.b

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=calculator(a,b)
print("Sum = ", c.add())
print()
print("Difference = ", c.sub())
print()
print("Quotient = " , c.div())
print()
print("Product = ", c.mul())
print()
