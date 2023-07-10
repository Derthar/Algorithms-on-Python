import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 1111))
sock.send('exits'.encode())

data = sock.recv(1024).decode()


print(data)
sock.close()