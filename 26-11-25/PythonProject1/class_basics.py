class Student:
    pass #do nothing

s1=Student()  #s1 is an object of class Student
s2=Student()

class Student1:
    def __init__(self, name, age): #Constructor; self is the object of the current class
        self.name=name
        self.age=age



s3=Student1("Krittika", 22)
print(s3.name, s3.age)

s4=Student1("Hari", 30)
