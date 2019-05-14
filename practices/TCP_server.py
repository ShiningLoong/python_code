import socket
import threading


def target_func(sock, addr):
    sock.send('who are you?'.encode('utf8'))
    while True:
        name = sock.recv(1024)
        if data and data != 'exit'.encode('utf8'):
            sock.send('Hello, %s' % name.encode('utf8'))
        else:
            break
            sock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(backlog=10)
while True:
    sct, ads = s.accept()
    t = threading.Thread(target=target_func, args=(sct, ads))
    t.start()

