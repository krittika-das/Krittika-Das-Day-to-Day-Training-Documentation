import pandas as pd
df=pd.read_csv("sales_data.csv")
f_df=df[df["Product"].str.contains("a", case=False, na=False)]
print(f_df)