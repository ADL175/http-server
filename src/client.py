"""This is the client socket for our echo application."""

import socket
import sys

def client(message):
    """."""
    address_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message += '*'
    client.sendall(message.encode('utf8'))

    buffer_length = 64
    message = b''

    while True:
        part = client.recv(buffer_length)
        message += part

        if '*' in message:
            break

    client.close()
    return message

if __name__ == '__main__': #pragma: no cover
    """."""
    message = sys.argv[1]
    client(message)
