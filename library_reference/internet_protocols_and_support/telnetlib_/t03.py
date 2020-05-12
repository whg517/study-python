# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t03
@Date: 2018/12/18 10:27
@Description:
"""
import time
import json

__author__ = 'wanghuagang'

import telnetlib

HOST = "localhost"
PORT = '6023'

EOF = b'\r\r\r\n>>> \r\r\r\n>>> '

# tn = telnetlib.Telnet(HOST, PORT)
# time.sleep(1)
# print(tn.read_very_eager())
# tn.read_until(b'\x1bc>>> \x1b[4h')
# tn.write(b"est()\n\n")
#
# # est = tn.read_until(EOF, timeout=3).decode('ascii')
# est = tn.read_until(EOF, timeout=3)
# print(est.decode('ascii'))

EST = b'p(stats.get_stats())'

ENTER = b'\n\n'

# tn.write(EST + ENTER)
# stats = tn.read_until(EOF, timeout=3)

stats = b"p(stats.get_stats())\r\r\r\n{'log_count/CRITICAL': 4,\r\r\r\n 'log_count/DEBUG': 3,\r\r\r\n 'log_count/INFO': 8,\r\r\r\n 'start_time': datetime.datetime(2018, 12, 19, 1, 28, 13, 928666)}\r\r\r\n>>> \r\r\r\n>>> "

stats_decode = stats.decode('ascii')
print(stats)

stats_replaced = stats_decode.replace('p(stats.get_stats())', '').replace('>>>', '').replace('\r', '').replace('\n',
                                                                                                               '').replace(
    "'", '"')

stats_json = json.loads(stats_replaced)
print(stats_json)

# tn.close()

b''.decode()
