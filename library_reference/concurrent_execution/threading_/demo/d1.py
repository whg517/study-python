import threading

# 返回当前活动的对象数。返回的计数等于返回 `enumerate()` 列表的长度
print(threading.active_count())

# 返回当前 Thread 对象，对于调用者的控制线程。如果未通过 `threading` 模块创建调用者的线程，
# 则返回具有有限功能的虚拟线程对象
print(threading.current_thread())

