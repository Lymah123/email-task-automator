from email_parser import EmailParser
import sys

def test_connection():
    print("Testing Gmail connection...")
    print("Step 1: Initializing connection...")
    parser = EmailParser()
    print("Step 2: Authenticating...")
    print("Step 3: Checking mailbox access...")
    parser.mail.select('INBOX')
    print("✓ Connection test completed successfully!")
    return parser

if __name__ == "__main__":
    test_connection()
