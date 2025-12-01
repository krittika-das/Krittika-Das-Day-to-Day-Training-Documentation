import pandas as pd

data = {
    "Name": ["Aishi", "Rahul", "Kritz"],
    "Marks": [23, 45, 55],
    "City": ["Mumbai", "Kolkata", "Delhi"]
}

df=pd.DataFrame(data)

df.to_csv("test.csv", index=False)

print("CSV created!")