import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ps111",
    database="retail_db"
)

orders_query = "SELECT order_id, customer_name, product_id, quantity, price FROM orders"
orders = pd.read_sql(orders_query, conn)

products = pd.read_csv("products.csv")

merged = pd.merge(orders, products, on="product_id", how="left")


merged["revenue"] = merged["quantity"] * merged["price"]

plt.figure(figsize=(8,5))
sns.barplot(x="category", y="revenue", data=merged, estimator=sum, ci=None)
plt.title("Revenue by Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_dashboard.png")
plt.show()

top_customers = merged.groupby("customer_name")["revenue"].sum().nlargest(5).reset_index()

with pd.ExcelWriter("final_report.xlsx", engine="openpyxl") as writer:
    merged.to_excel(writer, sheet_name="Orders", index=False)
    top_customers.to_excel(writer, sheet_name="Top_Customers", index=False)
