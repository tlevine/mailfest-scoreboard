'''
Each of these functions takes an
email.message.Message and returns
a string, boolean, float or int.
Or None.
'''
import re as _re
from io import StringIO as _StringIO
from tokenize import generate_tokens as _generate_tokens

def _ilen(iterable) -> int:
    'Calculate the length iteratively.'
    return sum(1 for _ in iterable)

def body_characters(email) -> int:
    'Number of characters in the body'
    return len(email.get_payload())

def body_words(email) -> int:
    'Number of words in the body'
    return _ilen(_generate_tokens(_StringIO(email.get_payload()).readline))

def body_lines(email) -> int:
    'Number of lines in the body'
    return _ilen(1 for _ in email.get_payload() if _ == '\n')

'''
def to_addresses(email) -> int:
    'Number of addresses in the "To:" field'
    return len(email.get_all('to'))

def cc_addresses(email) -> int:
    'Number of addresses in the "CC:" field'
    return len(email.get_all('cc'))
'''

def hops(email) -> int:
    'Number of "Received" headers in the email'
    return len(email.get_all('received'))

def subject_re(email) -> bool:
    'Whether the subject indicates a reply (starts with /^re:/)'
    subject = email.get('subject')
    return _re.match(r'^re:.*$', subject, flags = _re.IGNORECASE) != None

def subject_fwd(email) -> bool:
    'Whether the subject indicates a forward (starts with /^fwd:/)'
    subject = email.get('subject')
    return _re.match(r'^fwd:.*$', subject, flags = _re.IGNORECASE) != None

def gmail(email) -> bool:
    '''
    Whether the email was sent from a Gmail address
    (whether the earliest/lowest "Received:" header includes "google.com ")
    '''
    return 'google.com ' in email.get_all('received')[-1]
