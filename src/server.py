"""This is the server socket for our echo application."""

import socket
import sys
from email.utils import formatdate


def response_ok():
    message = b'HTTP/1.1 200 OK\r\n\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    return message + b'\r\n\r\n'


def response_error():
    return b'HTTP/1.1 500 Internal Server Error\r\n\r\n'

def server():
    """."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    server.listen(1)

    while True:
        try:
            connection, address = server.accept()

            buffer_length = 8
            message_complete = False
            message = ''

            while not message_complete:
                part = connection.recv(buffer_length).decode()
                message += part

                if message.endswith('\r\n\r\n'):
                    print(message)
                    response = response_ok()
                    connection.sendall(response)
                    connection.close()
                    break

        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """."""
    print('Your echo server is up and running')
    server()
