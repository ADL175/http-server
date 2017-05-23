import pytest
from client import client
"""
messages shorter than one buffer in length
messages longer than several buffers in length
messages that are an exact multiple of one buffer in length
messages containing non-ascii characters
"""

CLIENT_TABLE = [
    ('hello'),
    ('hello there, I am over 16'),
    ('abcdefghabcdefgh'),
    ('áÇÈ')
]

@pytest.mark.parametrize('message', CLIENT_TABLE)
def test_client(message):
    assert client(message) == message
