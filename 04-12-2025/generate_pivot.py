import pandas as pd
from datetime import datetime
df=pd.read_csv("retail.csv")

df['Sales']=df['TotalPrice']*df['Quantity']
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.month

pivot=df.pivot_table(index='Category',columns='Month',values='Sales', aggfunc='sum')
print(pivot)