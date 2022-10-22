import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self,tasks):
        self.tasks = tasks
        with open('taski.json','w', encoding="utf-8") as f:
            json.dump(self.tasks, f)
