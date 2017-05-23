"""This is the client socket for our echo application."""

import socket
import sys

def client(message):
    """."""
    address_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))

    buffer_length = 64
    reply_complete = False
    message = b''

    while not reply_complete:
        part = client.recv(buffer_length)
        message += part

        if len(part) < buffer_length:
            print(message.decode('utf8'))
            break

if __name__ == '__main__':
    """."""
    message = sys.argv[1]
    client(message)