import socket


s = socket.socket()
s.bind(('localhost',1234))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!","utf-8"))