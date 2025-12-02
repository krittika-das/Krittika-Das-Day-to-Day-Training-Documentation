import pandas as pd
df=pd.read_csv("sales_data.csv")
avfg_revenue=df.groupby("CustomerType")["TotalPrice"].mean()
print(avfg_revenue)