import pandas as pd
df=pd.read_csv("retail.csv")
df['Sales']=df['TotalPrice']*df['Quantity']
clean_df=df.copy()
for col in ['TotalPrice', 'Quantity', 'Sales']:
    q1=clean_df[col].quantile(0.25)
    q3=clean_df[col].quantile(0.75)
    IQR=q3-q1
    lower=q1-1.5*IQR
    upper=q3+1.5*IQR
    clean_df=clean_df[(clean_df[col]>=lower) & (clean_df[col]<=upper)]

print(clean_df)

