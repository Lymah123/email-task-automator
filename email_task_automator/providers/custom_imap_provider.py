from .base_provider import BaseEmailProvider
import imaplib

class CustomIMAPProvider(BaseEmailProvider):
    def __init__(self, credentials):
        self.email = credentials['email']
        self.password = credentials['password']
        self.server = credentials['server']

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.server)
        self.connection.login(self.email, self.password)

