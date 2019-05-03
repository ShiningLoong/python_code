# -*- coding:utf-8 -*-
import threading
import time
num = 0


def func1(name):
    global num
    print("hello", name)  # do sth without accessing common data
    with lock:
        func_single("t1")
        time.sleep(10)
        func_single("t1")
    print("num after thread1 is %d" % num)


def func2(name):
    global num
    print("hello", name)
    with lock:
        func_single("t2")


def func_single(name):  # do sth singly
    print("%s is calling" % name)
    global num
    print("start to change num")
    num += 1
    print("change done")


lock = threading.Lock()
t1 = threading.Thread(target=func1, args=("A",))
t2 = threading.Thread(target=func2, args=("B",))
if __name__ == "__main__":
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("finally num is %d" % num)

# 1.to keep a common data safe (not be changed unexpectedly), we would better to get a lock before change it
# 2.if threadA already acquire the lock, threadB can still do everything, UNLESS  threadB also try to get the lock.
