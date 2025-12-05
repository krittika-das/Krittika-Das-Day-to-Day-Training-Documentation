import pymysql
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Memories000%",
    database="subscription_app"
)
df = pd.read_sql("SELECT * FROM subscriptions", conn)
conn.close()

print(df)

df["days_left"] = pd.to_datetime(df["expiry_date"]) - pd.Timestamp.today()
df["age_days"] = pd.Timestamp.today() - pd.to_datetime(df["start_date"])

df["days_left_days"] = df["days_left"].dt.days
df["age_days_days"] = df["age_days"].dt.days

print(df[df["days_left_days"].between(0, 7)])

def status(row):
    days_left = row["days_left_days"]
    if days_left < 0:
        return "Expired"
    elif days_left <= 7:
        return "ExpiringSoon"
    else:
        return "Active"

df["status"] = df.apply(status, axis=1)

print(df["status"].value_counts())

print(df[df["days_left_days"].between(0, 7)])
print(df[df["days_left_days"] < 0])

price_map = {
    "Monthly": 1000,
    "Quarterly": 2700,
    "Yearly": 10000
}
df["renewal_value"] = df["plan_type"].map(price_map)

forecast = df[df["days_left_days"] <= 30]["renewal_value"].sum()
print("Projected Revenue:", forecast)

print(df)