# -*- coding: utf-8 -*-
import socket
import chardet
import sys
import io
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

buff = []
while True:
    d = s.recv(1024)
    if d:
        buff.append(d)
    else:
        break
s.close()
response = b''.join(buff)
print(response)
string = response.decode("utf8").encode('gbk').decode('gbk')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  #跟操作系统相关，一般不建议更改
print(string)
# # print(response.decode('utf-8'))
# # print(chardet.detect(response))
# with open(r'C:\baidu.html', 'xb+') as f:
#     f.write(response)


"______________________________________________________________________"

# string = "百度"
# bt = string.encode('utf-8')
# print(bt)
# print(bt.decode('utf-8'))
# bt = '奥斯卡咖啡'.encode('utf-8')

print(bt)