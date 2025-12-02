import pandas as pd
df=pd.read_csv('sample.csv')
filtered_data=df.sort_values('Sales', ascending=False)
print(filtered_data)

filtered_data=df.sort_values('Profit', ascending=True)
print(filtered_data)

filtered_data=df.sort_values(['Region', 'City'])
print(filtered_data)

filtered_data=df.sort_values('CustomerName')
print(filtered_data)