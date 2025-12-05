from datetime import datetime,timedelta, date

dob="16-10-2003"
d=datetime.strptime(dob,'%d-%m-%Y').date()
t=date.today()

year=t.year-d.year
month=t.month-d.month
day=t.day-d.day

if day<0:
    month=month-1
    day=day+30
if month<0:
    year=year-1
    month=month+12

print(f"{year} years, {month} months, {day} days")