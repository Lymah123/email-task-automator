import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from email_parser import EmailParser
from task_manager import TaskManager
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'demo-key-123'
socketio = SocketIO(app, async_mode='eventlet')

class EmailTaskAutomator:
    def __init__(self):
        self.parser = EmailParser()
        self.task_manager = TaskManager()
        self.start_monitoring()

    def start_monitoring(self):
        def check_emails():
            while True:
                new_emails = self.parser.parse_emails()
                for email in new_emails:
                    task = self.process_email(email)
                    if isinstance(task['deadline'], datetime.datetime):
                        task['deadline'] = task['deadline'].strftime('%Y-%m-%d %H:%M:%S')
                    socketio.emit('new_task', task, namespace='/')
                eventlet.sleep(10)

        eventlet.spawn(check_emails)

    def process_email(self, email_data):
        return {
            'subject': email_data['subject'],
            'deadline': email_data['deadline'],
            'priority': 'High',
            'created_at': datetime.datetime.now().strftime("%H:%M:%S")
        }

@app.route('/')
def index():
    return render_template('live_demo.html')

@app.route('/tasks')
def get_tasks():
    automator = EmailTaskAutomator()
    tasks = automator.task_manager.get_all_tasks()
    for task in tasks:
        if isinstance(task.get('deadline'), datetime.datetime):
            task['deadline'] = task['deadline'].strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(tasks)

if __name__ == '__main__':
    automator = EmailTaskAutomator()
    socketio.run(app, debug=True)
