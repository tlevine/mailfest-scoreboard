import imaplib

class Mailbox:
    def __init__(self, host, address, password):
        self.address = address
        self.M = imaplib.IMAP4_SSL(host)
        self.M.login(address, password)
        self.M.select('INBOX')

    def close(self):
        self.M.close()
        self.M.logout()

    def wipe(self):
        'Delete all emails in the account.'

        # Molly guard
        if self.address != 'mailfest@thomaslevine.com':
            result = raw_input('Warning: Everything in %s will be deleted. Continue? (Type "yes".)')
            if result != 'yes':
                self.close()
                exit(1)

        # Delete everythin
        typ, data = self.M.search(None, 'ALL')
        for num in data[0].split():
           self.M.store(num, '+FLAGS', '\\Deleted')
        self.M.expunge()

    def delete(self, num):
        'Delete the email with a particular number.'
        self.M.store(num, '+FLAGS', '\\Deleted')
        self.M.expunge()

    def peek(self):
        'Look at an arbitrary email.'
        typ, data = self.M.search(None, 'ALL')
        nums = data[0].split()

        # Read the first one if it's available.
        if nums != []:
            num = nums[0]
            typ, data = self.M.fetch(num, '(RFC822)')
            return data[0][1]
