import pandas as pd
df=pd.read_csv("sales_data.csv")
result=df.groupby("Store")["TotalPrice"].sum()
print(result)
result=df.groupby("City")["TotalPrice"].sum()
print(result)
result=df.groupby("Category")["TotalPrice"].sum()
print(result)
