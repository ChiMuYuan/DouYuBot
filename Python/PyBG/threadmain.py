import time, socket
from threading import *
from PyBG import keepalive, readdanmu, GloVar


class threadmain():
    def __init__(self):
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Socket.connect(("openbarrage.douyutv.com", 8601))
        self.kp = keepalive.keepalive(Socket)
        self.rc = readdanmu.recivedata(Socket)

    def run(self):
        self.kp.start()
        self.rc.start()
