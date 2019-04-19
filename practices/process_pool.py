import os
import time
import random
from multiprocessing import Pool


def f(name):
    start_time = time.time()
    print("process %s is running,pid is %s" % (name, os.getpid()))
    time.sleep(random.random()*3)
    end_time = time.time()
    print("process %s ran in %s " % (name, (end_time-start_time)))


if __name__ == "__main__":
    p = Pool(5)
    for i in range(5):
        p.apply_async(f, args=(i,))
    p.close()
    p.join()
