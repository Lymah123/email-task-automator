from abc import ABC, abstractmethod

class BaseEmailProvider(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_emails(self):
        pass
