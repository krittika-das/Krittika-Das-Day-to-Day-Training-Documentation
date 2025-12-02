import pandas as pd
df=pd.read_csv("sales_data.csv")
df=df.sort_values(["Date", "TotalPrice"], ascending=[True, True])
print(df)