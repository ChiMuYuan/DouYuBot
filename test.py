import socket
HOST='127.0.0.1'
PORT=8888
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
while 1:
    data=conn.recv(1024)
    data = data.decode()
    if data == "ok":
        break
    data = data.split('[')[1].split(']')[0].split(',')
    for i in range(len(data)):
        data[i] = data[i].split('\'')[1].split('\'')[0]
    print(data)
    conn.sendall(("Done").encode())

conn.close()
