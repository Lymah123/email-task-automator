from .providers.gmail_provider import GmailProvider
from .providers.outlook_provider import OutlookProvider
from .providers.yahoo_provider import YahooProvider
from .providers.custom_imap_provider import CustomIMAPProvider

class EmailProviderFactory:
    providers = {
        'gmail': GmailProvider,
        'outlook': OutlookProvider,
        'yahoo': YahooProvider,
        'custom': CustomIMAPProvider
    }

    @classmethod
    def get_provider(cls, provider_name, credentials):
        return cls.providers[provider_name](credentials)
