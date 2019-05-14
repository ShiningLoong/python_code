# coding: utf8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
data = []
while True:
    d = s.recv(1024)
    if d:
        data.append(d)
    else:
        break
response = b''.join(data).decode('utf8')
print(response)

