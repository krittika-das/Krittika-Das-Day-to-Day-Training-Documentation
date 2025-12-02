import pandas as pd
df=pd.read_csv("sales_data.csv")
result=(df[df["Quantity"]>=2].query("Category=='Apparel'").assign(TotalValue= lambda x: x['Quantity'] * x["UnitPrice"]).sort_values("TotalValue", ascending=False).reset_index(drop=True))
print(result)