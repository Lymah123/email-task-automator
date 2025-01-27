# Email Task Automator

Email Task Automator is a Python web application that monitors an email inbox for deadline-related emails and processes them to create tasks. It also provides a web interface to view the tasks and their statistics.

## Features

- Monitors an email inbox for new tasks
- Processes emails to extract task information
- Provides a web interface to view tasks and statistics
- API endpoint to receive data via webhooks

## Requirements

- Python 3.7+
- Flask
- Flask-RESTful
- requests
- schedule
- imaplib
- colorama

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/email-task-automator.git
    cd email-task-automator/email_task_automator
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `EMAIL_CONFIG` dictionary in `email_parser.py` with your email server details and credentials:

```python
EMAIL_CONFIG = {
    'imap_server': 'imap.example.com',
    'email': 'your-email@example.com',
    'password': 'your-password'
}
```

## Running the Application

  1. Start the email monitoring script:

  `python main.py`

  2. Start the web interface:
  `python web_interface.py`

  3. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the task dashboard.

  ## API Endpoint
- `GET /dashboard`: Returns the list of tasks, statistics, and upcoming deadlines.
- `POST /webhook`: Receives data via webhooks and forwards it to Agent.ai.

## Example of Usage

To test the webhook endpoint, you can use `curl`:

```
curl -X POST http://localhost:5000/webhook -H "Content-Type: application/json" -d "{\"user_input\":\"test data\"}"

```


## Using ngrok for External Access
To expose your local server to the internet for testing webhooks:

1. Download and install ngrok from ngrok.com.

2. Start ngrok:
`ngrok http 5000`

3. Use the provided ngrok URL to test the webhook:
```
curl -X POST https://your-ngrok-url.ngrok.io/webhook -H "Content-Type: application/json" -d "{\"user_input\":\"test data\"}"

```


## Integrating with Agent.ai
1. **Register Your Webhook in Agent.ai**: Use the ngrok URL to register your webhook in Agent.ai. The URL should point to the `/webhook` endpoint of your Flask application. For example:

```
https://your-ngrok-url.ngrok.io/webhook
```

2. **Test the Integration**: You can test the integration by sending a POST request to your ngrok URL using curl or any other HTTP client:

```
curl -X POST https://your-ngrok-url.ngrok.io/webhook -H "Content-Type: application/json" -d "{\"user_input\":\"test data\"}"
```

