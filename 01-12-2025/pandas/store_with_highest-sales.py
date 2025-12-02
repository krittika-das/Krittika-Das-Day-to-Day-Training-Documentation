import pandas as pd
df=pd.read_csv("sales_data.csv")
mp=df.loc[df["TotalPrice"].idxmax()]
sname=mp["Store"]
print("Higest store value: ", sname)