from typing import Dict

import csv
import sys, os
import getpass
from time import sleep

from email import message_from_bytes

import feed
import stats
from headers import headers

fields = [
    "from",
    "date",
    "to_addresses",
    "cc_addresses",
    "user-agent",
    "content-type",
    "hops",
    "binary_attachments",
    "subject_re",
    "subject_fwd",
    "body_characters",
    "body_words",
    "body_lines",
    "gmail",
]

def read_email(email:bytes) -> dict:
    'Compute all the statistics.'
    parsed_email = message_from_bytes(email)
    features = {}

    # Headers
    features.update(headers(parsed_email))

    # Statistics
    stat_names = filter(lambda x: not x.startswith('_'), dir(stats))
    features.update({stat_name: getattr(stats, stat_name)(parsed_email) \
        for stat_name in stat_names})

    return features

def credentials() -> Dict[str,str]:
    'Get the email account credentials.'
    c = {
        'host': os.environ.get('MAILFEST_IMAP_HOST', 'mail.gandi.net'),
        'address': os.environ.get('MAILFEST_ADDRESS', 'mailfest@thomaslevine.com'),
        'password': os.environ.get('MAILFEST_PASSWORD'),
    }
    if not c['password']:
         c['password'] = getpass.getpass('Password for %s:' % c['address'])
    return c

def main():
    if not os.path.exists('mailfest.csv'):
        with open('mailfest.csv', 'w') as results:
            w = csv.DictWriter(results, fields)
            w.writeheader()

    M = feed.Mailbox(**credentials())
    while True:
        with open('mailfest.csv', 'a') as results:
            num, email = M.peek()
            if num == None:
                sleep(10)
            else:
                email_stats = read_email(email)
                w = csv.DictWriter(results, fields)
                w.writerow(email_stats)
                M.delete(num)
