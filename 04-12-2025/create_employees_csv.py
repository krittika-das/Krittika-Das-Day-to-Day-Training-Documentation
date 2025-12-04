import csv
employees = ["ID", "Name", "Salary"]
for i in range(1, 21):
    employees.append([i, f"Emp{i}", 3000+i*100])

with open('employees.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(employees)

data=[]
with open('employees.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

print(data)