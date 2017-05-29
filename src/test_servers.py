# -*- coding: utf-8 -*-
"""Test HTTP server."""

import pytest


# # Echo server tests
# LESS_THAN_BUFFER_LENGTH_TABLE = [
#     ('yes yes', 'yes yes'),
#     ('no no', 'no no'),
#     ('what what', 'what what')
# ]
#
# LONGER_THAN_SEVERAL_BUFFER_LENGTHS_TABLE = [
#     ('here is a string that is long', 'here is a string that is long'),
#     ('and here is another string that is very long', 'and here is another string that is very long')
# ]
#
# EXACT_BUFFER_LENGTH_TABLE = [
#     ('here is a string', 'here is a string'),
#     ('12345678', '12345678'),
#     ('1234567812345678', '1234567812345678')
# ]
#
# NON_ASCII_CHAR_TABLE = [
#     ('!@#$%^&', '!@#$%^&'),
#     ('?:;<>$@', '?:;<>$@')
# ]
#
# @pytest.mark.parametrize('message_sent, message_received', LESS_THAN_BUFFER_LENGTH_TABLE)
# def test_client_less_than_buffer_length(message_sent, message_received):
#     """This tests the echo server with less than one buffer length."""
#     from client import client
#     assert client(message_sent) == message_received
#
#
# @pytest.mark.parametrize('message_sent, message_received', LONGER_THAN_SEVERAL_BUFFER_LENGTHS_TABLE)
# def test_client_longer_than_several_buffer_lengths(message_sent, message_received):
#     """This tests the echo server with longer than several buffer lengths."""
#     from client import client
#     assert client(message_sent) == message_received
#
#
# @pytest.mark.parametrize('message_sent, message_received', EXACT_BUFFER_LENGTH_TABLE)
# def test_client_exact_buffer_length(message_sent, message_received):
#     """This tests the echo server with exact buffer length."""
#     from client import client
#     assert client(message_sent) == message_received
#
#
# @pytest.mark.parametrize('message_sent, message_received', NON_ASCII_CHAR_TABLE)
# def test_client_non_ascii(message_sent, message_received):
#     """This tests the echo server with non ascii characters."""
#     from client import client
#     assert client(message_sent) == message_received

# Step 1 tests

def test_response_ok():
    """Assert if response_ok() returns a valid HTTP response."""
    valid = True
    from server import response_ok
    response = response_ok()
    if response.startswith(b'HTTP/1.1 200 OK'):
        response_list = response.split(b'\r\n')
        response_list = response_list[1:]
        response_list = [line for line in response_list if line is not b'']

        for line in response_list:
            if not (line.startswith(b'Date:') or line.startswith(b'Content-Type') or line.startswith(b'Content-Length')):
                valid = False

        assert valid


def test_response_error():
    """Asssert if response_error() returns a valid HTTP error response"""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 Internal Server Error\r\n\r\n'