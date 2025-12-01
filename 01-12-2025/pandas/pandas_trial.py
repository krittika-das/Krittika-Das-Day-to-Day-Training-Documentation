import pandas as pd

s=pd.Series([10, 20, 30, 40])
print(s)

data={
    "Name": ["Sara", "Krittika", "Vandita"],
    "Roll No.": [23, 45, 55]
}

print(pd.DataFrame(data))