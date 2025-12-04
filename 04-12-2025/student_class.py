class Student:
    def __init__(self,sid,name, marks):
        self.sid=sid
        self.name=name
        self.marks=marks
    def cal_grade(self):
        if self.marks>90:
            return "A"
        elif self.marks>80:
            return "B"
        elif self.marks>70:
            return "C"
        else:
            return "F"

s=Student(101,"Anaiyya",92)
print(s.name, " Grade: ")
print(s.cal_grade())