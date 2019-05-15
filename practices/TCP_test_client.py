# coding: utf8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
# s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# data = []

while True:
    d = s.recv(1024)
    print(d.decode('utf8'))
    msg = input()
    s.send(msg.encode("utf8"))
    print('已发送')
# response = b''.join(data).decode('utf8')
# print(response)

