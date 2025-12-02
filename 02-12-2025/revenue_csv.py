import pandas as pd
df=pd.read_csv('revenue.csv')
print(df.head(5))

print(df.info())
print(df.describe())

print(df.isnull().sum())

df["Date"]=pd.to_datetime(df["Date"])

print(df.info())

df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day

print(df)
print(df.info())