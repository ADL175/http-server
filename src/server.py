"""This is the server socket for our echo application."""

import socket
import sys
from email.utils import formatdate
import os
import io


ROOT_DIRECTORY = './'


def resolve_uri(uri):
    """
    Implement a function called resolve_uri that will take as an argument the URI parsed from a request.
    It will return a body for a response and an indication of the type of content contained in the body (as a tuple).
    """

    #- If the resource identified by the URI is a directory,
    # return a simple HTML listing of that directory as the body.
    if os.path.isdir(uri):
        uri_contents = os.listdir(uri)
        listing_string =
        for item in uri_contents:
            listing_string += item + '\n'
        print(listing_string)
        return listing_string
    # - If the resource identified by the URI is a file, return the contents of the file as the body.
    elif os.path.isfile(uri):
        uri_file = io.open(uri, 'rb')
        # file_size = os.getsize(uri)
        return uri_file.read()

    # - The content type value should be related to the type of file.
    # - If the requested resource cannot be found, raise an appropriate Python exception.


def parse_request(request):
    """
    sample GET request:
    GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n
    """
    list_str = request.split('\r\n')
    list_str[0] = list_str[0].split()
    # list_str[1] = list_str[1].split()
    print(list_str)
    if list_str[0][0] == 'GET':
        if list_str[0][2] == 'HTTP/1.1':
            if 'Host:' in list_str[1]:
                return list_str[0][1]

            else:
                print('get host error')
                raise ValueError('Invalid host syntax')

        else:
            print('get http error')
            raise ValueError('Wrong HTTP type')

    else:
        print('get error')
        raise ValueError('Should be GET request')



def response_ok():
    message = b'HTTP/1.1 200 OK\r\n\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    return message + b'\r\n\r\n'


def response_error(error_code, reason):
    print('response error called')
    if error_code == '400' and reason == 'Bad Request':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')

    elif error_code == '401' and reason == 'Not Found':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')

    elif error_code == '500' and reason == 'Server Error':
        response = 'HTTP/1.1 {} {}\r\n\r\n'.format(error_code, reason)
        return response.encode('utf8')



    # return b'HTTP/1.1 500 Internal Server Error\r\n\r\n'

def server():
    """."""
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
            message = ''

            while not message_complete:
                part = connection.recv(buffer_length).decode()
                message += part

                if message.endswith('\r\n\r\n'):

                    try:
                        print(parse_request(message))


                    except ValueError:
                        response = response_error('400', 'Bad Request')
                        connection.sendall(response)
                        connection.close()
                        break

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
