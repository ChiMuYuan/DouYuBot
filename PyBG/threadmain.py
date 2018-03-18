import time
import socket
from threading import *
from PyBG import keepalive


class threadmain():
    def __init__(self,):
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Socket.connect(("openbarrage.douyutv.com", 8601))
        kp = keepalive.keepalive(Socket)
        # rc =

    # def run(self):
