import pytz
from datetime import datetime

utc = pytz.UTC
print(utc)
sh = pytz.timezone('Asia/Shanghai')
print(sh)


time = datetime(2019, 2, 5, 10, 00, 00, tzinfo=utc)
print(time)

local_time = time.astimezone(sh)
print(local_time)
