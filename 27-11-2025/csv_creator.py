import csv
data=[["name", "marks"], ["Rohan", 88], ["Priya", 92], ["Amit", 79]]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("Succesfully written")