from datetime import date, datetime, timedelta

dates=["2025-09-08", "2025-07-19", "2025-08-26"]

m=[]
for k in dates:
    c=datetime.strptime(k, "%Y-%m-%d").date()
    m.append(c)

print(m)