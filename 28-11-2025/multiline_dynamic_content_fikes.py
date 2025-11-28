def write_file(emp_id, name, salary):
    record = f"""
    Employee record:
    ID: {emp_id},
    Name: {name},
    Salary: {salary}
    """
    with open("employee.txt", "a") as f:
        f.write(record)

write_file(101, "Krittika", 35000)
write_file(102, "Sara", 30000)
