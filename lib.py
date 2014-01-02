import imaplib

class Mailbox:
    def __init__(self, host, address, password):
        self.address = address
        self.M = imaplib.IMAP4(host)
        self.M.login(address, password)
        self.M.select('INBOX')

    def close(self):
        M.close()
        M.logout()

    def wipe(self):
        'Delete all emails in the account.'
        if self.address != 'mailfest@thomaslevine.com':
            result = raw_input('Warning: Everything in %s will be deleted. Continue? (Type "yes".)')
            if result != 'yes':
                self.close()
                exit(1)

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
        if nums == []:
        else:
            typ, data = M.fetch(nums[0], '(RFC822)')
            print 'Message %s\n%s\n' % (num, data[0][1])

