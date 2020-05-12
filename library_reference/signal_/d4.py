import signal
import sys
import time


def handler(signum, frame):
    print('闹钟')
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

while True:
    time.sleep(1)
    print("学习python中...")
