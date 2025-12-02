import pandas as pd
df=pd.read_csv('revenue.csv')

high_ele=df[(df["Category"] == "Electronics") & (df["TotalPrice"]>10000)]
print(high_ele)

sorted_df=df.sort_values("TotalPrice", ascending=False)

category_sales = df.groupby("Category")["TotalPrice"].sum()
print(category_sales)

store_avg = df.groupby("Store")["TotalPrice"].mean()
print(store_avg)

city_orders=df.groupby("City")["TotalPrice"].count()
print(city_orders)