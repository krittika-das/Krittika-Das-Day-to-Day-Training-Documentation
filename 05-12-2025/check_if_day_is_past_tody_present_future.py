from datetime import timedelta, datetime
g=datetime.strptime("2025-01-01","%Y-%m-%d").date()
today=datetime.today().date()
if g<today:
    print('Past')
elif today<g:
    print('Future')
else:
    print('Today')
