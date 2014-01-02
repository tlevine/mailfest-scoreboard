KEYS = [
    'from',
    'date',
    'content-type',
    'user-agent',
]

def headers(email):
    return {key: email.get(key) for key in KEYS}
