import pandas as pd

df=pd.read_csv("revenue.csv")
print(df.columns)
customers = pd.DataFrame({
    'CustomerType': ["New", "Returning"],
    'Discount': [5, 10]
})
merged=df.merge(customers, on="CustomerType", how="left")
print(merged)