from datetime import datetime, timedelta
dt=datetime.strptime('01/01/2019','%d/%m/%Y')
print((dt+timedelta(days=3)).date())