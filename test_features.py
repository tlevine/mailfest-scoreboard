import os
from email import message_from_file

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
