import pandas as pd
df=pd.read_csv("sample.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
df["ShippingDate"]=df["ShipDate"] - df["OrderDate"]
print(df)

print(df.info())
df["ProfitMargin"] = df["Profit"] // df['Sales']
print(df)

df["CustomerName"] = df["CustomerName"].str.title()
print(df)

df=df[df["Sales"]>0]
print(df)

df["Discount"]=df["Discount"]*100
print(df)