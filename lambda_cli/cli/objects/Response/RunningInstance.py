from .BaseInstance import BaseInstance

class RunningInstance:
    def __init__(self, json_object) -> None:
        self.id = json_object["id"]
        self.status = json_object["status"]
        self.ip = json_object["ip"]
        self.instance = BaseInstance(json_object["instance_type"])
        self.jupyter_url = json_object.get("jupyter_url", None)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.instance.name} {self.ip} ({self.status}) {self.instance.price_dollar}$ per hour"
