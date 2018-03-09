#Client

import socket
from cookies import *
from ConfigPackage import *

def sendCookies():
    RC = ReadConf.RCConf("./ConfigPackage/")
    IP = RC.getIP()
    PORT = RC.getPORT()
    sendData = googlecookies.getcookies()
    sendData.append("room_id")
    sendData.append(str(RC.getroom_id()))
    sendData.append("nickname")
    sendData.append(RC.getnickname())
    Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Socket.connect((IP,PORT))
    Socket.sendall(str(sendData).encode())
    recvdata = Socket.recv(1024)
    recvdata = recvdata.decode()
    Socket.sendall("ok".encode())
    Socket.close()
    return recvdata