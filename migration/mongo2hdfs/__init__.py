from datetime import datetime

import pytz

if __name__ == '__main__':
    utc = pytz.UTC
    shanghai = pytz.timezone('Asia/Shanghai')

    utc_date = datetime(2019, 1, 1, tzinfo=utc)
    local_date = utc_date.astimezone(shanghai)

    print(local_date)

    shanghai_date = datetime(2019,1,1, tzinfo=shanghai)
    print(shanghai_date)


"""
输出

2019-01-01 08:00:00+08:00
2019-01-01 00:00:00+08:06
"""

"""
注意：
直接使用 `Asia/Shanghai` 时区，会出现 tzinfo 为 `+0806` 的情况。
这是新老时区规定造成的。

正确的使用姿势为 `utc_date.astimezone(shanghai)`
"""
