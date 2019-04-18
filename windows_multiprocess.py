# usage of multiprocess in windows platform
# how to create a sub process
from multiprocessing import Process
import os


def fun_proc(name):
    print("sub proc %s is running with pid %s, parent proc's pid is %s" % (name, os.getpid(), os.getppid()))

# There will be an error if don't use __name__ == "__main__"
# in order to avoid unintendedly forking a subprocess
# p = Process(target=fun_proc, args=("sub1",))
# p.start()
# p.join()

#
# if __name__ == "__main__":
#     p = Process(target=fun_proc, args=("sub1",))
#     p.start()
#     p.join()


# what if I create subprocess in a function

def create_child():
    p = Process(target=fun_proc, args=("sub1",))
    p.start()
    p.join()

# the excution of the func that create subproc still need to follow if __name__ == "__main__" :


if __name__ == "__main__" :
    create_child()
