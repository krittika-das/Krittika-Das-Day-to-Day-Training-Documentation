from datetime import datetime, timedelta

def exp(l):
    today=datetime.today().date()
    limit=today+timedelta(days=15)
    r=[]

    for d in l:
        dt=datetime.strptime(d,"%Y-%m-%d").date()
        if today<=dt<=limit:
            r.append(d)
    return r

d=["2025-01-10", "2025-01-20", "2025-02-02"]
print(exp(d))