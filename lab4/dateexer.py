#1
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago:", five_days_ago)

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Date time without microseconds:", current_datetime_without_microseconds)

#4
from datetime import datetime

date1 = datetime(2022, 1, 1, 0, 0, 0)
date2 = datetime(2022, 1, 2, 0, 0, 0)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)
