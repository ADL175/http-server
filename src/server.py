"""This is the server code for an HTTP server."""

import socket
import sys
from email.utils import formatdate


def response_ok():
    """Return a valid HTTP response."""
    message = b'HTTP/1.1 200 OK\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    message += b'\r\nContent-Type: text/plain\r\n\r\n'
    return message


def response_error():
    """Return an internal error response."""
    return b'HTTP/1.1 500 Internal Server Error\r\n\r\n'

def server():
    """Listens for message and returns an HTTP response."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5028)

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


                if message.endswith(b'\r\n\r\n'):
                    break

            print(message.split(b'\r\n\r\n')[0])
            connection.sendall(response_ok())
            connection.close()

        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """Server code that will in console."""
    print('Your HTTP server is up and running')
    server()
