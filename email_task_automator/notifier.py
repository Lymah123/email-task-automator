from notifiers import DesktopNotifier, EmailNotifier, SlackNotifier, MobileNotifier

class NotificationManager:
    def __init__(self):
        self.channels = {
            'desktop': DesktopNotifier(),
            'email': EmailNotifier(),
            'slack': SlackNotifier(),
            'mobile': MobileNotifier()
        }

    def send_notification(self, task, channels=['desktop']):
        for channel in channels:
            self.channels[channel].notify(task)
