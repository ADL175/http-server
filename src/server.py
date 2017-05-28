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
    """Server set up to receive message from client and echo message back to client."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)

    address = ('127.0.0.1', 5010)
    server.bind(address)
    server.listen(1)

    while True:
        try:
            connection, address = server.accept()

            buffer_length = 8
            message_complete = False
            message = b''

            while not message_complete:
                part = connection.recv(buffer_length)
                message += part

                if b'*' in message:
                    break

            connection.sendall(message)
            connection.close()

        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """This block of code will run from console."""
    print('Your echo server is up and running')
    server()
