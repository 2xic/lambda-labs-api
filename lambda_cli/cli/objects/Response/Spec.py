
class Spec:
    def __init__(self, json_object):
        self.vcpus = json_object["vcpus"]
        self.memory_gib = json_object["memory_gib"]
        self.storage_gib = json_object["storage_gib"]
