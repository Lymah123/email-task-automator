from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

# Add these routes here
@app.route('/')
def home():
    return "Welcome to the Task Management API! Access /dashboard to view the data."

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with HTTP status code 204 (No Content)

class TaskManager:
    def get_all_tasks(self):
        # Implement Agent.ai task fetching logic here
        return self.fetch_tasks_from_agent()

    def fetch_tasks_from_agent(self):
        return []

class TaskAnalytics:
    def get_summary(self):
        # Placeholder implementation
        return {}

class DeadlineTracker:
    def get_upcoming(self):
        # Placeholder implementation
        return []

class TaskDashboard(Resource):
    def get(self):
        return {
            'tasks': TaskManager().get_all_tasks(),
            'statistics': TaskAnalytics().get_summary(),
            'upcoming_deadlines': DeadlineTracker().get_upcoming()
        }

class AgentWebhook(Resource):
    def post(self):
        data = request.get_json()
        agent_ai_url = 'https://api-lr.agent.ai/v1/agent/vn8uf6cbdydf2hos/webhook/f8aaa995'
        response = requests.post(agent_ai_url, json={'user_input': data})
        return {'status': 'success', 'received': data, 'agent_ai_response': response.json()}

# Add the TaskDashboard endpoint
api.add_resource(TaskDashboard, '/dashboard')

# Add the AgentWebhook endpoint
api.add_resource(AgentWebhook, '/webhook')

if __name__ == '__main__':
    print("Starting the web server...")
    app.run(debug=True)
