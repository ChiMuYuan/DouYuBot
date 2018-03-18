
from PyBG import DouYucode, senddanmu
from threading import *

class recivedata(Thread):
    def __init__(self, Socket):
        Thread.__init__(self)
        self.Socket = Socket
        self.flag = True
        self.send = True

    def run(self):
        a = "type@=loginreq/roomid@=74751/"
        b = "type@=joingroup/rid@=74751/gid@=-9999/"
        while True:
            if self.flag:
                data = self.Socket.recv(10240)
                result = DouYucode.decodeBin(data)
                # if result[1].find("#抢分") != -1 and self.send:
