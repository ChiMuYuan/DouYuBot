import socket, time
from ConfigPackage import *
from PyBG import GloVar

HOST = '127.0.0.1'
PORT = 8888
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.bind((HOST, PORT))
Socket.listen(1)
print("[%s] 启动程序" % (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))))
while True:
    conn,addr = Socket.accept()
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data == "ok":
            break
        data = data.split('[')[1].split(']')[0].split(',')
        for i in range(len(data)):
            data[i] = data[i].split('\'')[1].split('\'')[0]
        acf_username = acf_ltkid = acf_stk = room_id = nickname = ""
        for i in range(len(data)):
            if data[i] == "acf_username":
                acf_username = data[i + 1]
            elif data[i] == "acf_ltkid":
                acf_ltkid = data[i + 1]
            elif data[i] == "acf_stk":
                acf_stk = data[i + 1]
            elif data[i] == "room_id":
                room_id = data[i + 1]
            elif data[i] == "nickname":
                nickname = data[i + 1]
        WriteConf.WConf("./ConfigPackage/", acf_username, acf_ltkid, acf_stk, room_id, nickname)
        conn.sendall(("Done").encode())
        sendIP = conn.getpeername()
        print("[%s] 接受到%s:%d发送的信息" %(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())), sendIP[0],
                                     sendIP[1]))
        # while True:
        #     try:
        #         GloVar.setMain(False)
        #         print("[%s] 重新启动程序" % (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))))
        #         GloVar.setMain(True)
        #         break
        #     except Exception:
        #         print("[%s] 启动失败" % (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))))
    conn.close()