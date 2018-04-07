import time
from PyBG import DouYucode, senddanmu, GloVar
from threading import *

class recivedata(Thread):
    def __init__(self, Socket):
        Thread.__init__(self)
        self.Socket = Socket

    def run(self):
        a = "type@=loginreq/roomid@=74751/"
        b = "type@=joingroup/rid@=74751/gid@=-9999/"
        self.Socket.sendall(DouYucode.encodeBin(a))
        self.Socket.sendall(DouYucode.encodeBin(b))
        GloVar.setWAIT(True)
        while True:
            data = self.Socket.recv(10240)
            result = DouYucode.decodeBin(data)
            nowt = int(time.time()) % 1800
            if result[1].find("#抢分") != -1 and GloVar.getWAIT():
                GloVar.setWAIT(False)
                senddanmu.senddamu("#抢分 " + time.strftime("%H:%M:%S", time.localtime(time.time())) + " 我就不信抢不到了")
                Thread(target=GloVar.resetWAIT(), daemon=True)
            # elif nowt <= 30 or 1730 <= nowt and GloVar.getWAIT():
            #     GloVar.setWAIT(False)
            #     senddanmu.senddamu("#签到 " + time.strftime("%H:%M:%S", time.localtime(time.time())) + " 艰苦赚分")
            #     Thread(target=GloVar.resetWAIT(), daemon=True)
            elif result[1].find("#签到") != -1 and GloVar.getWAIT():
                GloVar.setWAIT(False)
                senddanmu.senddamu("#签到 " + time.strftime("%H:%M:%S", time.localtime(time.time())) + " 艰苦赚分")
                Thread(target=GloVar.resetWAIT(), daemon=True)