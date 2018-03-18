#Client

import socket
from cookies import *
from ConfigPackage import *

def sendCookies():
    print("2")
    RC = ReadConf.RCConf("./ConfigPackage/")
    print("3")
    IP = RC.IP
    PORT = RC.PORT
    print("4")
    sendData = googlecookies.getcookies()
    sendData.append("room_id")
    sendData.append(str(RC.room_id))
    sendData.append("nickname")
    sendData.append(RC.nickname)
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.connect((IP,PORT))
    print("t")
    Socket.sendall(str(sendData).encode())
    recvdata = Socket.recv(1024)
    recvdata = recvdata.decode()
    Socket.sendall("ok".encode())
    Socket.close()
    return recvdata