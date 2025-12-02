import pandas as pd
df=pd.read_csv("sample.csv")
print(df.head(10))
rows, col=df.shape
print("Noo. of Rows: ", rows)
print("Noo. of Columns: ", col)
print(df.dtypes)
print(df.isnull().sum())

df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())