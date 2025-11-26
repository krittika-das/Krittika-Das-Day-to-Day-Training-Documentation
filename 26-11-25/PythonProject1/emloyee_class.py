class Employee:
    def __init__(self,emp_id,name, dept, salary):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary
    def display(self):
        print(self.emp_id, self.name,self.dept,self.salary)

e1=Employee(101, "Alice",'HR',20000)
e2=Employee(102, "Bob",'Tech',40000)
e1.display()
print()
e2.display()
