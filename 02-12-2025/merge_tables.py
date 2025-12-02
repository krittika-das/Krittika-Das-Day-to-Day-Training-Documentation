import pandas as pd
df=pd.read_csv("sample.csv")
dl=pd.DataFrame({'Segment': ['Consumer', 'Corporate', 'Home office'],
                 'Discount': [5, 8, 10]
                 })

df=df.merge(dl, on='Segment', how='left')
print(df)

tr=pd.DataFrame({'Region': ['East', 'West', 'South', 'Central'],
                 'Tax': [5, 2, 7, 8]
                 })
df=df.merge(tr, on='Region', how='left')
print(df)

customer_totals=df.groupby('CustomerID').agg({'Sales': 'sum',
                                              'Quantity': 'sum'}).reset_index()
customer_totals.rename(columns={'Sales': 'Total_Sales', 'Quantity': 'Total_Quantity'}, inplace=True)
df=df.merge(customer_totals, on='CustomerID', how='left')
print(df)