import os
from .objects.Response.NewInstance import NewInstance
from typing import Union, List
import json

class Database:
    def __init__(self) -> None:
        self.path = os.path.join(
            os.path.dirname(__file__),
            "database.json"
        )
    
    def add_instance(self, instance: Union[NewInstance, List[NewInstance]]):
        instances: List[NewInstance] = instance if type(instance) == list else [instance]
        data = self.read()
        for i in instances:
            if i.id not in data:
                data.append(i.id)
        self.write(data)

    def remove_instance(self, instance):
        instances: List[NewInstance] = instance if type(instance) == list else [instance]
        data = self.read()
        for i in instances:
            if i.id in data:
                data.remove(i.id)
        self.write(data)

    def read(self):
        if os.path.isfile(self.path):
            with open(self.path, "r") as file:
                return json.load(file)
        return []

    def write(self, data: List[str]):
        with open(self.path, "w") as file:
            json.dump(data, file)
