"""This is the client socket for our echo application."""

import socket
import sys

def client(message):
    """Client sends request to server."""
    message = 'GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n'
    address_info = socket.getaddrinfo('127.0.0.1', 5005)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message += '\r\n\r\n'
    client.sendall(message.encode('utf8'))

    buffer_length = 8
    message = ''

    while True:
        part = client.recv(buffer_length).decode()
        message += part

        if message.endswith('\r\n\r\n'):
            break

    client.shutdown(socket.SHUT_WR)
    client.close()
    print(message[:-1])
    return message[:-1]

if __name__ == '__main__': #pragma: no cover
    message = sys.argv[1]
    client(message)
