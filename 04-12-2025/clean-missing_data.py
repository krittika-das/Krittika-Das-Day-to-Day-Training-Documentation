import pandas as pd
df=pd.read_csv("retail.csv")

numcols=df.select_dtypes(include=['int64', 'float64']).columns
cat=df.select_dtypes(include=['object']).columns

df[numcols]=df[numcols].fillna(df[numcols].median())
df[cat]=df[cat].fillna(df[cat].mode().iloc(0))

print(df.head(10))
print(df.isnull().sum())
