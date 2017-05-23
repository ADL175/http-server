import socket


def server():
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)

    address = ('127.0.0.1', 5000)

    server.bind(address)

    server.listen(1)

    connection, address = server.accept()

    while not reply_complete:
        part = connection.recv(buffer_length)
        print(part.decode('utf8'))

        if len(part) < buffer_length:
            break

    message = "I hear you, loud and clear!"
    connnection.sendall(message.encode('utf8'))


if __name__ == '__main__':
    """."""
    import sys
    server()
