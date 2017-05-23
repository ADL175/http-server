"""This is the server socket for our echo application."""

import socket
import sys


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

            buffer_length = 64
            message_complete = False
            message = b''
            while not message_complete:
                part = connection.recv(buffer_length)
                message += part

                if len(part) < buffer_length:
                    break

            connection.sendall(message)
            connection.close()

        except KeyboardInterrupt:
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """."""
    print('Your echo server is up and running')
    server()
