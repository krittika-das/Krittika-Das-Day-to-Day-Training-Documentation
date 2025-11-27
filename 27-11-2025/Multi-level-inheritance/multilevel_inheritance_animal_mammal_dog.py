class Animal:
    def locomotion(self):
        print("All animals can move")
    def eat(self):
        print("Eating animal")

class Mammal(Animal):
    def __init__(self, mammals):
        self.mammals = mammals
    def young(self):
        print("All ", self.mammals,  " give birth")

class Dog(Mammal):
    def bark(self):
        print("Barking ", self.mammals)

x=Dog("mammals")
x.locomotion()
x.eat()
x.young()
x.bark()
