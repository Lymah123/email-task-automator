from .base_provider import BaseEmailProvider
import imaplib

class GmailProvider(BaseEmailProvider):
    def __init__(self, credentials):
        self.email = credentials['email']
        self.password = credentials['password']
        self.server = 'imap.gmail.com'

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.server)
        self.connection.login(self.email, self.password)
