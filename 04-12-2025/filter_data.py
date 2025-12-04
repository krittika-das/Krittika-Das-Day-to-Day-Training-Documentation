import pandas as pd
df=pd.read_csv("retail.csv")

df['Sales']=df['TotalPrice']*df['Quantity']
cs=df.groupby('Category')['Sales'].sum()
print(cs)