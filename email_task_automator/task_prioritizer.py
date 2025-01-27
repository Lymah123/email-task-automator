from datetime import datetime
from dateutil.relativedelta import relativedelta, FR

class SmartDateParser:
    def parse_date(self, text):
        patterns = {
            'relative': {
                'next week': lambda: datetime.now() + relativedelta(weeks=1),
                'end of month': lambda: datetime.now() + relativedelta(day=31),
                'coming friday': lambda: datetime.now() + relativedelta(weekday=FR)
            },
            'specific': r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:\s+\d{4})?)',
            'iso': r'\d{4}-\d{2}-\d{2}'
        }
        return self.extract_best_date(text, patterns)
