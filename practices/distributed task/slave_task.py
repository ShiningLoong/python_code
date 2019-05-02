# -*- coding: utf-8 -*-
from multiprocessing.managers import BaseManager
import queue


class TaskManager(BaseManager):
    pass


TaskManager.register("get_task")
TaskManager.register("get_result")
slave = TaskManager(address=("127.0.0.1", 5000), authkey=b"abcd")
slave.connect()

task = slave.get_task()
result = slave.get_result()
for i in range(10):
    t = task.get(timeout=10)
    result.put(t**2)
    print("put %d into result" % t**2)
slave.shutdown()


