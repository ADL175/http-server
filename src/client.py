"""This is the client socket for our echo application."""

import socket
import sys

def client(message_to_send):
    """Client set up to send message to server."""
    address_info = socket.getaddrinfo('127.0.0.1', 5010)
    stream_info = [i for i in address_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message_to_send += '*'
    client.sendall(message_to_send.encode('utf8'))

    buffer_length = 8
    message_received = b''

    while True:
        part = client.recv(buffer_length)
        message_received += part

        if b'*' in message_received:
            break

    client.shutdown(socket.SHUT_WR)
    client.close()
    print(message_received[:-1].decode())
    return message_received[:-1].decode()

if __name__ == '__main__': #pragma: no cover
    """This block of code will run from console."""
    message_to_send = sys.argv[1]
    client(message_to_send)
