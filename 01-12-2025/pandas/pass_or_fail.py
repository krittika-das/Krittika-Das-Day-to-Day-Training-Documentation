import pandas as pd

df=pd.read_csv("test.csv")
print(df)

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x>50 else "Fail")
print(df)

sorted_df=df.sort_values("Marks", ascending=False)
print(sorted_df)