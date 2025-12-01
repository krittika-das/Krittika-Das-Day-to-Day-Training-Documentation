import pandas as pd
df=pd.read_csv("sales_data.csv")
df["Date"]=pd.to_datetime(df["Date"])
df["year"]=df["Date"].dt.year
df["month"]=df["Date"].dt.year
df["day"]=df["Date"].dt.day

print(df["year"])
print(df["month"])
print(df["day"])