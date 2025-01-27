from .base_provider import BaseEmailProvider
import imaplib

class YahooProvider(BaseEmailProvider):
    def __init__(self, credentials):
        self.email = credentials['email']
        self.password = credentials['password']
        self.server = 'imap.mail.yahoo.com'

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.server)
        self.connection.login(self.email, self.password)
