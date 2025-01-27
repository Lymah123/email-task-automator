from email_parser import EmailParser
from task_manager import TaskManager
import time
import schedule
import datetime
import colorama
from colorama import Fore, Style

colorama.init()

def process_emails():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n{Fore.CYAN}[{current_time}] 🔍 Scanning inbox...{Style.RESET_ALL}")

    parser = EmailParser()
    task_manager = TaskManager()
    new_tasks = parser.parse_emails()

    if new_tasks:
        print(f"{Fore.GREEN}✨ Found {len(new_tasks)} new tasks!{Style.RESET_ALL}")
        for task in new_tasks:
            print(f"\n{Fore.YELLOW}📌 Task Details:{Style.RESET_ALL}")
            print(f"📧 Subject: {task['subject']}")
            print(f"👤 From: {task['sender']}")
            print(f"⏰ Deadline: {task['deadline']}")
    else:
        print(f"{Fore.BLUE}📭 Inbox checked - No new tasks{Style.RESET_ALL}")

def main():
    print(f"{Fore.GREEN}🚀 Email Task Automator is starting...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}✓ Checking emails every 5 minutes")
    print(f"✓ Monitoring for deadline-related emails")
    print(f"\n📊 Live Activity Log:{Style.RESET_ALL}")

    # Initial check
    process_emails()

    # Schedule regular checks
    schedule.every(5).minutes.do(process_emails)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
