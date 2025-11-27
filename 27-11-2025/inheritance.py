class Animal:
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def bark(self):
        print("I am a dog and I bark.")

d=Dog()
d.speak() #inherited
d.bark()    #child's own method