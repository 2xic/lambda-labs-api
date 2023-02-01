from typing import List

class RequestTerminateInstances:
    def __init__(self, ids: List[str]):
        self.ids = ids

    def payload(self):
        return {
            "instance_ids": self.ids
        }

