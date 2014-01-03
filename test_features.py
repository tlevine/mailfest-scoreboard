import os
from email import message_from_file
from email.message import Message
import builtins

import nose.tools as n

import headers, stats

email = message_from_file(open(os.path.join('fixtures','attachments')))

def test_headers():
    observed = headers.headers(email)
    expected = {
        'date': 'Thu, 2 Jan 2014 21:37:44 +0000',
        'from': 'Thomas Levine <_@thomaslevine.com>',
        'user-agent': 'Mutt/1.5.22 (2013-10-16)',
        'content-type': 'multipart/mixed; boundary="AqsLC8rIMeq19msA"'
    }
    n.assert_dict_equal(observed, expected)

def test_ilen():
    n.assert_equal(stats._ilen(range(100)), len(range(100)))

def test_body():
    n.assert_is_instance(stats._body(email), str)

def test_body():
    payload = stats._payload(email)
    n.assert_not_is_instance(payload, builtins.str)
    for bomb in payload:
        n.assert_is_instance(bomb, Message)
