"""This is the server socket for our echo application."""

import socket
import sys


def response_ok():
    return b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nSuccess*'


def response_error():
    return """
HTTP/1.1 500 Internal Server Error
Content-Type: text/plain
Server Error"""


def server():
    """."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)

    while True:
        try:

            connection, address = server.accept()

            buffer_length = 8
            message_complete = False
            message = ''

            while not message_complete:
                print('inside second while loop.')
                part = connection.recv(buffer_length).decode()
                message += part

                if len(part) < buffer_length:
                    break

            print(message[:-1])
            print(response_ok())
            connection.sendall(response_ok())
            connection.close()

        except KeyboardInterrupt:
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """."""
    print('Your echo server is up and running')
    server()
