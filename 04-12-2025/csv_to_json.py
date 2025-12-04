import json
import csv

d=[]

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        d.append(row)

with open("employees.json", "w") as f:
    json.dump(d, f, indent=4)