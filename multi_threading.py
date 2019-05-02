import threading
student = threading.local()


def process_std():
    print("thread %s is running,Hello %s!" % (threading.current_thread().name, student.name))


def thread_func(name):
    student.name = name
    process_std()


if __name__ == "__main__":
    p = threading.Thread(target=thread_func, args=("SpongeBob",))
    p.start()
