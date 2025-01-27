import socketio

def send_test_email():
    test_email = {
        'subject': 'Urgent: Project Deadline Tomorrow',
        'sender': 'manager@company.com',
        'content': 'Please complete the project report by tomorrow 5 PM.',
        'deadline': '2024-01-27 17:00:00'
    }
    socketio.emit('new_email', test_email)
