import pandas as pd
df=pd.read_csv('sample.csv')

filtered_df=df.groupby('Region')['Sales'].sum()
print(filtered_df)

filtered_df=df.groupby('Category')['Profit'].mean()
print(filtered_df)

filtered_df=df.groupby('CustomerName')['ProductName'].count()
print(filtered_df)

filtered_df=df.groupby('Segment')['Sales'].sum()
print(filtered_df)

filtered_df=df.groupby('SubCategory')['Quantity'].sum().reset_index(name='Total_Quantity')
print(filtered_df)

