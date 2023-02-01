from .Spec import Spec

class BaseInstance:
    def __init__(self, instances) -> None:
        self.name = instances["name"]
        self.price_cents_per_hour = instances["price_cents_per_hour"]
        self.description = instances["description"]
        self.specs = Spec(instances["specs"])

    def __repr__(self):
        return self.__str__()

    @property
    def price_dollar(self):
        return (self.price_cents_per_hour / 100)

