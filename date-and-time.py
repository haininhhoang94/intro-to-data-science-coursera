import datetime as dt
import time as tm

tm.time()

# get the timestamp for time now, and get each value from that timestamp
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second, dtnow.microsecond

delta = dt.timedelta(days=100)
delta

today = dt.date.today()
today

today - delta

today > today - delta
