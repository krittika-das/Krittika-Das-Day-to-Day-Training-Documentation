import pandas as pd

df=pd.read_csv("test.csv")

print(df)

print(df.head(2))
print(df.tail(2))

print(df.shape)
print(df.columns)
print(df.describe())

print(df["Name"])

#filters
highscore = df[df["Marks"] > 70]
print(highscore)

filtered = df[(df["Marks"] > 70) & (df["Marks"] < 100)]
print(filtered)
