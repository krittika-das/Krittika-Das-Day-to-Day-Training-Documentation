import pandas as pd
df=pd.read_csv("retail.csv")

df['Sales']=df['TotalPrice']*df['Quantity']
report=df.groupby('Category').agg(
    ts=('Sales', 'sum'),
    oc=('OrderID', 'count'),
    avgp=('TotalPrice', 'mean')
)

print(report)