from datetime import date, timedelta

t=date.today()
x=[(t + timedelta(days=i)).isoformat() for i in range(30)]
print(x)