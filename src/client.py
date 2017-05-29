"""This is the client code for an HTTP server."""

import socket
import sys


def client(message_to_send):
    """Sends message to server and receives an HTTP response."""
    message_to_send = 'GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n'
    address_info = socket.getaddrinfo('127.0.0.1', 5005)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message_to_send += '\r\n\r\n'
    client.sendall(message_to_send.encode('utf8'))

    buffer_length = 8
    message_received = ''

    while True:
        part = client.recv(buffer_length).decode()
        message_received += part

        if message_received.endswith('\r\n\r\n'):
            break

    client.shutdown(socket.SHUT_WR)
    client.close()
    print(message_received[:-1])
    return message_received[:-1]

if __name__ == '__main__':  # pragma: no cover
    """Module code that will run in console."""
    message = sys.argv[1]
    client(message)
