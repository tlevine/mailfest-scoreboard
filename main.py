from typing import Dict

import json
import sys, os
import getpass
from time import sleep

from email import message_from_bytes

import feed
import stats
from headers import headers

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
    M = feed.Mailbox(**credentials())
    while True:
        with open('mailfest.jsonlines', 'a') as results:
            num, email = M.peek()
            if num == None:
                sleep(10)
            else:
                email_stats = read_email(email)
                results.write(json.dumps(email_stats) + '\n')
                M.delete(num)
