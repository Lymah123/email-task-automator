import json
from datetime import datetime

class TaskManager:
  def __init__(self, tasks_file='tasks.json'):
    self.tasks_file = tasks_file
    self.tasks = self.load_tasks()

  def load_tasks(self):
      try:
        with open(self.tasks_file, 'r') as f:
          return json.load(f)
      except FileNotFoundError:
        return[]

  def save_tasks(self):
      with open(self.tasks_file, 'w') as f:
        json.dump(self.tasks, f, indent=4, default=str)

  def add_task(self, task):
      task_id = len(self.tasks) + 1
      task['id'] = task_id
      task['created_at'] = datetime.now().isoformat()
      task['status'] = 'pending'
      self.tasks.append(task)
      self.save_tasks()
      return task_id

  def get_all_tasks(self):
      return self.tasks

  def get_pending_tasks(self):
      return [task for task in self.tasks if task['status'] == 'pending']
