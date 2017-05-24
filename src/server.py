"""This is the server socket for our echo application."""

import socket
import sys


def response_ok():
    return b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nSuccess*'


def response_error():
    return b'HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\nServer Error*'

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
                print(message)
                part = connection.recv(buffer_length).decode()
                message += part

                if len(part) < buffer_length:
                    #break
                    response = response_ok()
                    # print(response)
                    # print(message[:-1])
                    # print(response_ok())
                    connection.sendall(response)
                    connection.close()
                    break

        except KeyboardInterrupt:
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__': # pragma: no cover
    """."""
    print('Your echo server is up and running')
    server()
