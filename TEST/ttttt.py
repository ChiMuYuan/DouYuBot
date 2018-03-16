import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
e = S.connect(("110.1.1.1", 10))
print(e)

