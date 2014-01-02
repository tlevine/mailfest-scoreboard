'''
Each of these functions takes an
email.message.Message and returns
a string, boolean, float or int.
Or None.
'''
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
    return _ilen(1 for _ in email.get_payload() if _ == '\n')
