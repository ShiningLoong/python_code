import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1999))
s.listen(10)
print('start listening')

def server_proc(sock, address):
    print('connection from %s:%s' % address)
    sock.send(b'Hello, who are you?')
    while True:
        d = sock.recv(1024)
        time.sleep(0.1)
        if not d or d.decode('utf8') == 'exit':
            break
        print(('%s:%s  %s') % (address[0], address[1],d.decode('utf8')))
        sock.send(('hello,%s!' % d.decode('utf8')).encode('utf8'))
    sock.close()
    print('connection closed by client.')

while True:
    sock, address = s.accept()
    t = threading.Thread(target=server_proc, args=(sock,address))
    t.start()









