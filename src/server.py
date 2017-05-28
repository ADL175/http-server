"""This is the server socket for our echo application."""

import socket
import sys


def server():
    """Server set up to receive message from client and echo message back to client."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5005)
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
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """."""
    print('Your echo server is up and running')
    server()
