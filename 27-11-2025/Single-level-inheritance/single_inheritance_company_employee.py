class Company:
    def __init__(self, name, location, x):
        self.name = name
        self.location = location
        self.x=x
    def profiles(self):
        return self.x

class Employee(Company):
    def __init__(self, name, location, emp_id, x, profile):
        super().__init__(name, location, x)
        self.emp_id = emp_id
        self.profile = profile
    def job_profile(self):
        for i in self.x:
            if i == self.profile:
                return True
        return False

a=Employee("Krittika", "Kolkata", 101, ["HR", "IT", "Dev", "Tester"], "Dev")
print("Available profiles: ", a.profiles())
print("Candidate sheet: ", a.name, ",", a.location, ",", a.profile)
if a.job_profile():
    print("Profile available")
else:
    print("Profile not available")