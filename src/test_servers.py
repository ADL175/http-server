# -*- coding: utf-8 -*-
"""Test echo server."""

import pytest


LESS_THAN_BUFFER_LENGTH_TABLE = [
    ('yes yes', 'yes yes'),
    ('no no', 'no no'),
    ('what what', 'what what')
]

LONGER_THAN_SEVERAL_BUFFER_LENGTHS_TABLE = [
    ('here is a string that is long', 'here is a string that is long'),
    ('and here is another string that is very long', 'and here is another string that is very long')
]

EXACT_BUFFER_LENGTH_TABLE = [
    ('here is a string', 'here is a string'),
    ('12345678', '12345678'),
    ('1234567812345678', '1234567812345678')
]

NON_ASCII_CHAR_TABLE = [
    ('!@#$%^&', '!@#$%^&'),
    ('?:;<>$@', '?:;<>$@')
]

@pytest.mark.parametrize('message_sent, message_received', LESS_THAN_BUFFER_LENGTH_TABLE)
def test_client_less_than_buffer_length(message_sent, message_received):
    """This tests the echo server with less than one buffer length."""
    from client import client
    assert client(message_sent) == message_received


@pytest.mark.parametrize('message_sent, message_received', LONGER_THAN_SEVERAL_BUFFER_LENGTHS_TABLE)
def test_client_longer_than_several_buffer_lengths(message_sent, message_received):
    """This tests the echo server with longer than several buffer lengths."""
    from client import client
    assert client(message_sent) == message_received


@pytest.mark.parametrize('message_sent, message_received', EXACT_BUFFER_LENGTH_TABLE)
def test_client_exact_buffer_length(message_sent, message_received):
    """This tests the echo server with exact buffer length."""
    from client import client
    assert client(message_sent) == message_received


@pytest.mark.parametrize('message_sent, message_received', NON_ASCII_CHAR_TABLE)
def test_client_non_ascii(message_sent, message_received):
    """This tests the echo server with non ascii characters."""
    from client import client
    assert client(message_sent) == message_received
