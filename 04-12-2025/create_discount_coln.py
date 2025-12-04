import pandas as pd
df=pd.read_csv("retail.csv")

df['Discounted_Price']=df['TotalPrice']*0.90
print(df)