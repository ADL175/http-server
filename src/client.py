"""This is a client socket"""

import socket


def client(message):
    """."""
    address_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))

    buffer_length = 8
    reply_complete = False
    msg = b''

    while not reply_complete:
        part = client.recv(buffer_length)
        msg += part

        if len(part) < buffer_length:
            print(msg.decode('utf8'))
            break


if __name__ == '__main__':
    """."""
    import sys
    message = sys.argv[1]
    client(message)
