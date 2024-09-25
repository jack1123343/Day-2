from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import date
from calendar import isleap

dt = datetime(2024, 9, 25, 9, 25, 47)
print(dt)

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.time())

t = time(9, 47, 00)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

delta = timedelta(days = 5 ,hours = 3, seconds = 30)
print("Time Delta ", delta)
today = date.today()
print("Before Date ", today)
future_date = today + delta
print("After Date ", future_date)

date1 = datetime(5, 4, 5, 3,23,52)
date2 = datetime(3, 1, 13, 12, 31, 13)
print(date1 - date2)

print(isleap(2024))