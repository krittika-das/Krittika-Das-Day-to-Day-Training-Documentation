import pandas as pd
s=pd.read_csv("sales_data.csv")
print(s["PaymentMethod"].value_counts())
