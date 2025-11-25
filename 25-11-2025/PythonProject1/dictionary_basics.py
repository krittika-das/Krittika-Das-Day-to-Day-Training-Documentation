student={
    "name": "Krittika",
    "age": 30,
    "city": "Kolkata"
}

print(student["name"])
print(student["age"])
#print(student["email"])

print(student.get("email"))

student["email"] = "krittika.das@gds.ey.com"

print(student.get("email"))

student["city"]="Dubai"
print(student.get("city"))

student.pop("city")
del student["email"]
student.clear()

student={
    "name": "Krittika",
    "age": 30,
    "city": "Kolkata"
}

#print keys amd values
for k in student.keys():
    print(k)

for v in student.values():
    print(v)

for k, v in student.items():
    print(k, v)