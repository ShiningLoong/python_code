# -*- coding: utf-8 -*-
from multiprocessing.managers import BaseManager
import queue
import time
import random


class TaskManager(BaseManager):
    pass


task_queue = queue.Queue()
result_queue = queue.Queue()


def task_func():
    return task_queue


def result_func():
    return result_queue


# TaskManager.register("get_task", callable=task_func)
# TaskManager.register("get_result", callable=result_func)
TaskManager.register("get_task", result_queue)
TaskManager.register("get_result", task_queue)
my_manager = TaskManager(('127.0.0.1', 5000), authkey=b"abcd")

if __name__ == "__main__":
    my_manager.start()
    task = my_manager.get_task
    result = my_manager.get_result

    for i in range(10):
        n = random.random()*10
        task.put(n)
        print("put task %f" % n)
        time.sleep(0.5)

    for i in range(10):
        r = result.get(timeout=10)
        print("get result %f" % r)

    my_manager.shutdown()
    print("manager has ended")
