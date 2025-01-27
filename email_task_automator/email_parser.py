import email
import imaplib
import datetime
import re
from config import EMAIL_CONFIG, DEADLINE_KEYWORDS

class EmailParser:
    def __init__(self):
        self.mail = imaplib.IMAP4_SSL(EMAIL_CONFIG['imap_server'])
        self.mail.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])

    def extract_date(self, text):
        date_patterns = [
            r'\d{1,2}/\d{1,2}/\d{4}',
            r'\d{1,2}-\d{1,2}-\d{4}',
            r'\d{4}-\d{1,2}-\d{1,2}',
            r'tomorrow',
            r'next (monday|tuesday|wednesday|thursday|friday|saturday|sunday)',
        ]

        for pattern in date_patterns:
            match = re.search(pattern, text.lower())
            if match:
                if match.group() == 'tomorrow':
                    return datetime.datetime.now() + datetime.timedelta(days=1)
                return match.group()
        return None

    def decode_content(self, payload):
        encodings = ['utf-8', 'latin-1', 'ascii', 'iso-8859-1']
        for encoding in encodings:
            try:
                return payload.decode(encoding)
            except UnicodeDecodeError:
                continue
        return payload.decode('utf-8', errors='ignore')

    def parse_emails(self):
        print("Starting email check...")
        tasks = []
        self.mail.select(EMAIL_CONFIG['folder'])

        # Only fetch recent unread emails
        date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        _, message_numbers = self.mail.search(None, f'(SINCE {date} UNSEEN)')
        print(f"Found {len(message_numbers[0].split())} recent unread emails")

        for num in message_numbers[0].split():
            _, msg_data = self.mail.fetch(num, '(RFC822)')
            email_body = msg_data[0][1]
            email_message = email.message_from_bytes(email_body)

            subject = email_message['subject']
            sender = email_message['from']
            content = ""

            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == 'text/plain':
                        payload = part.get_payload(decode=True)
                        if payload:
                            content += self.decode_content(payload)
            else:
                payload = email_message.get_payload(decode=True)
                if payload:
                    content += self.decode_content(payload)

            for keyword in DEADLINE_KEYWORDS:
                if keyword in content.lower() or keyword in subject.lower():
                    deadline_date = self.extract_date(content) or self.extract_date(subject)
                    if deadline_date:
                        tasks.append({
                            'subject': subject,
                            'sender': sender,
                            'deadline': deadline_date,
                            'content': content[:200] + '...' if len(content) > 200 else content
                        })
                        break

        return tasks
