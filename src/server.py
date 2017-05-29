"""This is the server code for an HTTP server."""

import socket
import sys
from email.utils import formatdate

"""
sample GET request:
GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n
"""


def parse_request(request):
    """Take client's incoming request and parses request into list to check values against."""
    list_str = request.split('\r\n')
    list_str[0] = list_str[0].split()
    if list_str[0][0] == 'GET':
        if list_str[0][2] == 'HTTP/1.1':
            if 'Host:' in list_str[1]:
                return list_str[0][1]

            else:
                raise ValueError('Invalid host syntax')

        else:
            raise ValueError('Wrong HTTP type')

    else:
        raise ValueError('Should be GET request')


def response_ok():
    """Return a valid HTTP response."""
    message = b'HTTP/1.1 200 OK\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    message += b'\r\nContent-Type: text/plain\r\n\r\n'
    return message


def response_error(error_code, reason):
    """Responds to client with a response error."""
    if error_code == '400' and reason == 'Bad Request':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')

    elif error_code == '401' and reason == 'Not Found':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')

    elif error_code == '500' and reason == 'Server Error':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')

    else:
        return 'HTTP/1.1 400 Bad Request\r\n\r\n'


def server():
    """Server function to process client request."""
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

                if message.endswith(b'\r\n\r\n'):

                    try:
                        print(parse_request(message))
                        response = response_ok()
                        connection.sendall(response)
                        connection.close()
                        break

                    except ValueError:
                        response = response_error('400', 'Bad Request')
                        connection.sendall(response)
                        connection.close()
                        break

        except KeyboardInterrupt:
            server.shutdown(socket.SHUT_WR)
            server.close()
            print('Shutting down echo server...')
            sys.exit()


if __name__ == '__main__':  # pragma: no cover
    """Server code that will in console."""
    print('Your HTTP server is up and running')
    server()
