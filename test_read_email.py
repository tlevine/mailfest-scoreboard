import os

import main

def test_read_email():
    bytetext = open(os.path.join('fixtures','attachments')).read().encode('ascii')
    main.read_email(bytetext)
