
class NewInstance:
    def __init__(self, id: str) -> None:
        self.id = id
    
    def __str__(self):
        return f"instance id: {self.id}"
        
    def __repr__(self):
        return self.__str__()
