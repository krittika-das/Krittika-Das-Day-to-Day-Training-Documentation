import pandas as pd
df=pd.read_csv("sample.csv")
filtered_df=df[df['Region'] == 'West']
print(filtered_df)

filtered_df=df[(df["Category"] == 'technology') & (df['Sales']>400)]
print(filtered_df)

print(df.loc[df['Ret'] == 'Yes'], "ProductName")

df['ShipDate'] = pd.to_datetime(df['ShipDate'])
filtered_df=df[(df['Category']=='Furniture') & (df['ShipDate']>'2024-01-20')]
print(filtered_df)

filtered_df=df[df['Profit']<20]
print(filtered_df)