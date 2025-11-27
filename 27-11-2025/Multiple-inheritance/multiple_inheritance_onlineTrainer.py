class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    def display(self):
        print(self.name)
        print(self.age)
        print(self.subject)

class Content_creator:
    def __init__(self, medium):
        self.medium = medium
    def creation(self):
        print("Can use: ", self.medium)

class Online_teacher(Teacher, Content_creator):
    def __init__(self, name, age, subject, medium, internet):
        Teacher.__init__(self, name, age, subject)
        Content_creator.__init__(self, medium)
        self.internet = internet
    def speed_test(self):
        print("Available: ", self.internet, " GB")

x=Online_teacher("Krittika", 22, "Maths", "youtube", 16)
x.display()
x.speed_test()