class Person:
    def __init__(self, name):
        self.name=name

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age=age

e=Employee("Krittika", 22)
print(e.name)
print(e.age)