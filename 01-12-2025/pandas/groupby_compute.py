import pandas as pd
df=pd.read_csv("sales_data.csv")
result=df.groupby("Category")["Quantity"].sum()
print(result)