from multiprocessing import Process
import os


def target_func(name):
    print("this is a child,his pid is %s,and his parent pid is %s" % (os.getpid(), os.getppid()))
    print(name)


if __name__ == "__main__":    # protect entry point of main module
    p = Process(target=target_func, args=("childA",))
    p.start()
    p.join()    # what is join() used for?

# relative knownledge/questions:
# what does python interpreter do?   # https://tech.blog.aknin.name/2010/04/02/pythons-innards-introduction/
# what is GIL Global interpreter lock?

