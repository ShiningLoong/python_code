# -*-coding: utf-8 -*-
from multiprocessing.managers import BaseManager
import random
import queue

task_queue = queue.Queue()
result_queue = queue.Queue()


class TaskManager(BaseManager):
    pass


TaskManager.register("get_task", callable=lambda: task_queue)
TaskManager.register("get_result", callable=lambda: result_queue)
manager = TaskManager(address=('', 5000), authkey=b"abcd")

manager.start()
task = manager.get_task()
result = manager.get_result()

# do sth with queue on net
for i in range(10):
    task.put(i)
    print("put task %d" % i)

for i in range(10):
    r = result.get(timeout=10)
    print("task result is %d" % r)

manager.shutdown()
print("task queue ended")
