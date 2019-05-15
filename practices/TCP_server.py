import socket
import threading


def target_func(sock, addr):
    sock.send('who are you?'.encode('utf8'))
    while True:
        name = sock.recv(1024)
        if name != 'exit'.encode('utf8'):
            print("%s:%s:" % addr, name.decode('utf8'))
            sock.send(('Hello, %s' % name.decode('utf8')).encode('utf8'))
        else:
            break
    sock.close()
    print('subThread ended')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 8888)
s.bind(address)
s.listen(10)
print('Listening from %s:%s' % address)

while True:
    sct, ads = s.accept()
    t = threading.Thread(target=target_func, args=(sct, ads))
    t.start()

