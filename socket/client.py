#coding=utf-8
from __future__ import print_function

import socket
from time import sleep
conn=[]
def connect():
    for i in range(10):
        cd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cd.connect(('localhost', 8080))
        conn.append(cd)
        print("第" + str(i) + "个连接成功！")
        sleep(5)


if __name__ == '__main__':
    connect()
    sleep(500)

