from email_parser import EmailParser
from task_manager import TaskManager

class EmailTaskAutomator:
    def __init__(self):
        self.parser = EmailParser()
        self.task_manager = TaskManager()

    def process_incoming_email(self, email_event):
        """Convert email to task with priority and deadline"""
        task_data = self.parser.extract_task_info(email_event)
        return self.task_manager.create_task(task_data)

class AgentIntegration:
    def handle_webhook(self, email_event):
        automator = EmailTaskAutomator()
        task = automator.process_incoming_email(email_event)
        return {"status": "success", "task_created": task}
