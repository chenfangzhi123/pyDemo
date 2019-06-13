import os
import socket
import sys
from time import sleep

PORT = 9918

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sd.bind(('0.0.0.0', PORT))
sd.listen(5)
sleep(20)
print(os.getpid())
for i in range(10):
    if os.fork() == 0:
        print(os.getpid())
        sd.close()
        cd = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
        cd.connect(('127.0.0.1', PORT))
        print("CLIENT:" + str(i))
        sys.exit()
sockets = []
for i in range(10):
    (cd, address) = sd.accept()

    print("SERVER:" + str(i))
    sockets.append(cd)
    cd.shutdown(socket.SHUT_WR)
    cd.close()
sleep(500)
os.system("lsof -p %i" % (os.getpid(),))
# os.system("netstat -nt|grep :%i" % (PORT,))
