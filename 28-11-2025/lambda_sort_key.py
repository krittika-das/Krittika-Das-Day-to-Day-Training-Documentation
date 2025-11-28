people=[{"name": "Rahul", "age": 25},
        {"name": "Aisha", "age": 20},
        {"name": "Rahul", "age": 30}]

sorted_people=sorted(people, key=lambda x: x["age"])


print(sorted_people)