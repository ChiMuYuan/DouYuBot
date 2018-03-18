import socket
from threading import *
import time
import re
import uuid
import hashlib


class keepalive(Thread):
    def __init__(self, Socket):
        Thread.__init__(self)
        self.Socket = Socket

    def run(self):
        while True:
            self.Socket.sendall(sendmeesage("type@=mrkl/"))
            time.sleep(45)

def calcMessageLength(Str):
    return 4 + 4 + len(Str.encode("utf8")) + 1

def sendmeesage(Str):
    code = [0xb1, 0x02, 0x00, 0x00]
    end = 0
    lenth = [calcMessageLength(Str), 0, 0, 0]
    Str = bytearray(Str, "utf8")
    tot = bytearray()
    for i in lenth:
        tot.append(i)
    for i in lenth:
        tot.append(i)
    for i in code:
        tot.append(i)
    for i in Str:
        tot.append(i)
    tot.append(end)
    return tot

def sss(Str):
    Socket.sendall(sendmeesage(Str))

def showdm(data):
    mid = data.find(b'type@=chatmsg/')
    cqid = data.find(b'type@=bc_buy_deserve/')
    spid = data.find(b'type@=spbc/')
    # print("1", end="")
    if mid == 12:
        # print("2")
        nick = bytearray()
        txt = bytearray()
        # print(data)
        nid = data.index(b'nn@=')
        tid = data.index(b'txt@=')
        eid = data.index(b'/cid@=')
        # print(nid)
        # print(tid)
        for i in range(nid + 4, tid - 1):
            nick.append(data[i])
        for i in range(tid + 5, eid):
            txt.append(data[i])
        if nick.decode("utf8") == "iiSNN":
            print(nick.decode("utf8") + " : " + txt.decode("utf8"))


class recivedata(Thread):
    def __init__(self, Socket):
        Thread.__init__(self)
        self.Socket = Socket

    def run(self):
        while True:
            data = self.Socket.recv(10240)
            showdm(data)

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((socket.gethostbyname("openbarrage.douyutv.com"), 8601))

HOST_JSON = "[{\"ip\":\"119.90.49.90\",\"port\":\"8099\"},{\"ip\":\"119.90.49.106\",\"port\":\"8028\"},{\"ip\":\"119.90.49.87\",\"port\":\"8083\"},{\"ip\":\"119.90.49.105\",\"port\":\"8021\"},{\"ip\":\"119.90.49.104\",\"port\":\"8020\"},{\"ip\":\"119.90.49.86\",\"port\":\"8077\"},{\"ip\":\"119.90.49.86\",\"port\":\"8080\"},{\"ip\":\"119.90.49.89\",\"port\":\"8091\"},{\"ip\":\"119.90.49.91\",\"port\":\"8054\"},{\"ip\":\"119.90.49.103\",\"port\":\"8012\"},{\"ip\":\"119.90.49.102\",\"port\":\"8007\"},{\"ip\":\"119.90.49.107\",\"port\":\"8031\"},{\"ip\":\"119.90.49.88\",\"port\":\"8089\"},{\"ip\":\"119.90.49.110\",\"port\":\"8048\"},{\"ip\":\"119.90.49.101\",\"port\":\"8005\"},{\"ip\":\"119.90.49.103\",\"port\":\"8011\"},{\"ip\":\"119.90.49.110\",\"port\":\"8046\"},{\"ip\":\"119.90.49.104\",\"port\":\"8017\"},{\"ip\":\"119.90.49.89\",\"port\":\"8095\"},{\"ip\":\"119.90.49.105\",\"port\":\"8024\"},{\"ip\":\"119.90.49.86\",\"port\":\"8079\"},{\"ip\":\"119.90.49.86\",\"port\":\"8078\"},{\"ip\":\"119.90.49.109\",\"port\":\"8045\"},{\"ip\":\"119.90.49.95\",\"port\":\"8073\"},{\"ip\":\"119.90.49.103\",\"port\":\"8015\"},{\"ip\":\"119.90.49.104\",\"port\":\"8018\"},{\"ip\":\"119.90.49.107\",\"port\":\"8033\"},{\"ip\":\"119.90.49.92\",\"port\":\"8056\"},{\"ip\":\"119.90.49.93\",\"port\":\"8065\"},{\"ip\":\"119.90.49.92\",\"port\":\"8060\"}]";

SocketSDM = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SocketSDM.connect("119.90.49.89", 8092)

bbbbb = (socket.gethostbyname("119.90.49.89"), 8092)

timenow = str(time.time())
uuiddd = str(uuid.uuid4()).replace("-", "").upper()
lasttt = timenow + "7oE9nPEG9xXV69phU31FYCLUagKeYtsF" + uuiddd

md555 = hashlib.md5()
md555.update(lasttt.encode("utf8"))

# 1525503

vk = md555.hexdigest()
a = "type@=loginreq/roomid@=74751/"
b = "type@=joingroup/rid@=74751/gid@=-9999/"
loginInfo = "type@=loginreq/username@=39019270/ct@=0/password@=/roomid@=74751/devid@=" + uuiddd + "/rt@=" + timenow + "/vk@=" + vk + "/ver@=20150929/aver@=2017073111/ltkid@=57277600/biz@=1/stk@=ca7624a66b58d4ef/"

senddanmu = "type@=chatmessage/receiver@=0/content@=test/scope@=/col@=0/pid@=/p2p@=0/nc@=0/rev@=0/ifs@=0/"

# ka = keepalive(Socket)
# rd = recivedata(Socket)

SocketSDM.sendall(sendmeesage(loginInfo))

# rd.start()
# sss(a)
# sss(b)
# ka.start()

class sdmsend(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            ssssss = input()
            SocketSDM.sendall(sendmeesage(
                "type@=chatmessage/receiver@=0/content@=" + ssssss + "/scope@=/col@=0/pid@=/p2p@=0/nc@=0/rev@=0/ifs@=0/"))

sdmsss = sdmsend()
sdmsss.start()

while True:
    print(SocketSDM.recv(10240).replace(b'@A', b'@').replace(b'@S', b'/'))

