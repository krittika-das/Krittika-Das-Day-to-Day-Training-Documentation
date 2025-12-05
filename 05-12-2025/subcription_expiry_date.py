from datetime import datetime, timedelta
start=datetime.strptime("2016-07-30", "%Y-%m-%d")
expiry=start+timedelta(days=30)

print(expiry.date())