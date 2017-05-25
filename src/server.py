"""This is the server socket for our echo application."""

import socket
import sys
from email.utils import formatdate


def parse_request(request):
    """
    sample GET request:
    GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n
    """
    list_str = request.split()

    if list_str[0] == 'GET':
        if list_str[2] == 'HTTP/1.1':
            if list_str[3] == 'Host:':
                return list_str[1]





def response_ok():
    message = b'HTTP/1.1 200 OK\r\n\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    return message + b'\r\n\r\n'


def response_error(error_code, reason):
    if error_code == '401' and reason == 'Not Found':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')
    elif error_code == '500' and reason == 'Server Error':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')



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
