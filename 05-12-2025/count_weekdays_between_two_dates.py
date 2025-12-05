from datetime import date, datetime, timedelta
s=datetime.strptime("2025-01-02", "%Y-%m-%d")
e=datetime.strptime("2025-12-31", "%Y-%m-%d")
c=0
while s<=e:
    if s.weekday()<5:
        c+=1
    s+=timedelta(days=1)
print(c)