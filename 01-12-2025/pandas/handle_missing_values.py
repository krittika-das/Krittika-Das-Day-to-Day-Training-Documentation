import pandas as pd
df=pd.read_csv("test.csv")
print(df)
print()

df2=df.copy()
df2.loc[2, "Marks"]= None
print(df2)
print()
print(df2.isnull().sum())
print()

df2_filled=df2.fillna("Unknown")
print(df2_filled)