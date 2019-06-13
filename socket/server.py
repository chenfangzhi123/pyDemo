#coding=utf-8
from __future__ import print_function

import os
import socket
import sys


print(os.getpid())
def listen():
    PORT = 8080
    sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sd.bind(('0.0.0.0', PORT))
    sd.listen(50)
    return sd

con=[]
if __name__ == '__main__':
    s = listen()
    i = 1
    while True:
        (fd,add)=s.accept()
        con.append(fd)
        fd.shutdown(socket.SHUT_WR)
        print("第" + str(i) + "个连接成功！")
        i += 1
    sys.stdin.readline()

