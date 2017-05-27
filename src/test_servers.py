# -*- coding: utf-8 -*-
import pytest
from client import client
from server import server


# TESTS FOR ECHO!!!!

# CLIENT_TABLE = [
#     ('hello'),
#     ('hello there, I am over 16'),
#     ('abcdefghabcdefgh'),
#     ('áÇÈ')
# ]
#
# @pytest.mark.parametrize('message', CLIENT_TABLE)
# def test_client(message):
#     assert client(message) == message


# step 3 WIP test func:


def test_good_client_parse_request():
    """Test if the client's request is a good request."""
    from server import parse_request
    assert parse_request("GET /index.html HTTP/1.1\r\nHost: www.foo.combo") == 'index.html'


def test_response_ok():
    """Test response_ok()"""
    from server import response_ok
    assert response_ok() == b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nSuccess*'


def test_response_error():
    """Test response_error()"""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\nServer Error*'
