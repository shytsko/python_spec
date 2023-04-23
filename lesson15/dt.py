from datetime import date, time, datetime, timedelta


now = datetime.now()

delta = timedelta(days=0.5)

print(f"{now = }\t{now}")

d = now.replace(hour=now.hour+23)
print(f"{d = }\t{d}")



