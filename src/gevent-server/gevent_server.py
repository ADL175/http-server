"""This is the gevent concurrent server - same as server."""

import socket
import sys
from email.utils import formatdate
import os
import io



def resolve_uri(uri):
    """Server function to determine type of file and provide response."""
    current_dir = os.getcwd()
    content_type_dict = {
        'image': b'image/jpeg',
        'png': b'image/png',
        'txt': b'text/plain',
        'html': b'text/html'
    }

    content_length = os.path.getsize(uri)
    content_type = b''

    if os.path.isdir(uri):
        content_type = b'text/directory'
        uri_contents = os.listdir(os.path.join(current_dir, uri))

    elif os.path.isfile(uri):
        file_type = uri.split('.')[-1]
        content_type = content_type_dict.get(file_type)
        uri_contents = io.open(uri, 'rb').read()
    else:
        raise Exception(response_error(404, 'Not Found'))
    # return tuple thing
    return (content_type, content_length, uri_contents)


    """
    sample GET request:
    GET /index.html HTTP/1.1\r\nHost: www.foo.combo\r\n\r\n
    """


def parse_request(request):
    """Server func to split the client request to method, uri, version."""
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


def response_ok(response_body):
    """Server function to send response ok."""
    (content_type, content_length, uri_contents) = response_body
    message = b'HTTP/1.1 200 OK\r\n\r\n'
    message += u'Date: {}'.format(formatdate(usegmt=True)).encode('utf8')
    message += b'Content-Type: %s\r\n' % (content_type)
    message += b'Content_Length: %d\r\n\r\n' % (content_length)
    message += uri_contents + '\r\n\r\n'
    print(message)
    return message


def response_error(error_code, reason):
    """Server func to send response error."""
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
    """Server takes request by client."""
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
    """Run the server function and print to console."""
    print('Your echo server is up and running')
    server()