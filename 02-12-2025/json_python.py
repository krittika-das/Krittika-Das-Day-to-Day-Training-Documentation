import pandas as pd
df=pd.DataFrame({
    "Name": ["Aisha", "Rahul", "Krittika"],
    "Marks": [45, 89, 90],
    "City": ["Chennai", "Noida", "Kolkata"],
})

df.to_json("students.json")

print("JSON created")

df=pd.read_json("students.json")

print(df)