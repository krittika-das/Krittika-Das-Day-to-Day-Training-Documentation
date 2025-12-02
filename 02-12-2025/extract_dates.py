import pandas as pd
df=pd.read_csv("sample.csv")
df['OrderDate']=pd.to_datetime(df['OrderDate'])
df['Year']=df['OrderDate'].dt.year
df['Month']=df['OrderDate'].dt.month
df['Day']=df['OrderDate'].dt.day
df['DayOfWeek']=df['OrderDate'].dt.day_name()

df['ShipDate']=pd.to_datetime(df['ShipDate'])
df['ShippingDays']=(df['ShipDate']-df['ShipDate']).dt.days
delayedorder=df[df['ShippingDays'] > 5]
monthly_sales=df.groupby(df['OrderDate'].dt.to_period('M'))['Sales'].sum()
ms=monthly_sales.to_timestamp()
print(df)
print(ms)
