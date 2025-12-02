import pandas as pd
df=pd.read_csv("sample.csv")
pivot_df=df.pivot_table(
    index='Region',
    columns='Category',
    values='Sales'
)
print(pivot_df)

pivot_df=df.pivot_table(
    index='SubCategory',
    columns='Segment',
    values='Profit'
)
print(pivot_df)

pivot_df=df.pivot_table(
    index='Ret',
    columns='Region',
    values='ProductName',
    aggfunc='count'
)
print(pivot_df)

pivot_df=df.pivot_table(
    index='Category',
    values='UnitPrice',
    aggfunc='sum'
)
print(pivot_df)

df['OrderDate']=pd.to_datetime(df['OrderDate'])
df['Month']=df['OrderDate'].dt.to_period('M')
pivot_df=df.pivot_table(
    index='Month',
    columns='Region',
    values='Quantity',
    aggfunc='sum'
)
print(pivot_df)