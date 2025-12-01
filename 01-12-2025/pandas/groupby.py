import pandas as pd

df=pd.DataFrame({
    "Name": ["Aisha", "rahul", "Jain", "Imran", "Neha"],
    "Marks": [78, 65, 23, 90, 67],
    "City": ["Mumbai", "Chennai", "Mumbai", "Kolkata", "bangalore"],
    "Age": [22, 34, 67, 89, 99]
})

city_c=df.groupby("City")["Name"].count()
print(city_c)

city_c=df.groupby("City")["Marks"].mean()
print(city_c)