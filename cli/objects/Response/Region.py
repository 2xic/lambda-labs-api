
class Region:
    def __init__(self, json_object):
        self.name = json_object["name"]
        self.description = json_object["description"]
    