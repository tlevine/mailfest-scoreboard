import os
from email import message_from_file

email = message_from_file(open(os.path.join('fixtures','attachments')))
