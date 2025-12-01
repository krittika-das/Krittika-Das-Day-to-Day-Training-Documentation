import pandas as pd

df=pd.read_csv("sales_data.csv")
df["Discount"]=df.apply(lambda row: row["TotalPrice"]*0.10  if row["CustomerType"]=="Returning" else row["TotalPrice"]*0.05, axis=1)
print(df.head(5))