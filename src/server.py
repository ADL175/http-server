import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = ('127.0.0.1', 5000)

server.bind(address)

server.listen(1)

connection, address = server.accept()
