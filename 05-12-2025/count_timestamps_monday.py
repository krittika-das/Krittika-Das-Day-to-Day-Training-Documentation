from datetime import datetime

c=0
ts=["2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10"]
for t in ts:
    dt=datetime.strptime(t,"%Y-%m-%d")
    if dt.weekday()==0:
        c+=1
print(c)