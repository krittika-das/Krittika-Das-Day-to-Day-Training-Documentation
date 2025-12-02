import pandas as pd
df=pd.read_csv("sales_data.csv")
edf=df[df["Category"].str.lower()=="electronics"]
edf.to_csv("electronics_csv.csv",index=False)