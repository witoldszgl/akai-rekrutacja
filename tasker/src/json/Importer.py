import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        with open('taski.json', encoding="utf-8") as f:
            return json.load(f)

    def get_tasks(self):
        return self.read_tasks()
