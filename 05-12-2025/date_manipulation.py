from datetime import datetime, date, time, timedelta
today=date.today()
print(today)

print(today.day)
print(today.month)
print(today.year)

now=datetime.now()
print(now)

dob=date(1995, 8, 14)
print(dob)

now=datetime.now()
f=now.strftime("%d-%m-%Y %H:%M:%S")
print(f)