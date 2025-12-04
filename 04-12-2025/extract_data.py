import pandas as pd
df=pd.read_csv("retail.csv")
to=df['OrderID'].nunique()
tr=(df['TotalPrice']*df['Quantity']).sum()
top_5=df['Product'].value_counts().head(5)
print(to, tr)
print(top_5)