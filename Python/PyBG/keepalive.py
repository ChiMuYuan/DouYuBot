import time
from threading import *
from PyBG import DouYucode

class keepalive(Thread):
    def __init__(self, Socket):
        Thread.__init__(self)
        self.SC = Socket
        self.flag = True

    def setStop(self):
        self.flag = False

    def run(self):
        while True:
            if self.flag:
                self.SC.sendall(DouYucode.encodeBin("type@=mrkl/"))
                time.sleep(45)