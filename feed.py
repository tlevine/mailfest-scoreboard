from typing import Tuple
import imaplib

class Mailbox:
    def __init__(self, host:str, address:str, password:str):
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
            result = input('Warning: Everything in %s will be deleted. Continue? (Type "yes".)')
            if result != 'yes':
                self.close()
                raise UserWarning('Wiping the account was aborted.')

        # Delete everything
        typ, data = self.M.search(None, 'ALL')
        for num in data[0].split():
           self.M.store(num, '+FLAGS', '\\Deleted')
        self.M.expunge()

    def delete(self, num:int) -> None:
        'Delete the email with a particular number.'
        self.M.store(num, '+FLAGS', '\\Deleted')
        self.M.expunge()

    def peek(self) -> Tuple[int,str]:
        'Look at an arbitrary email.'
        typ, data = self.M.search(None, 'ALL')
        nums = data[0].split()

        # Read the first one if it's available.
        if nums == []:
            return None, None
        else:
            num = nums[0]
            typ, data = self.M.fetch(num, '(RFC822)')
            return num, data[0][1]
