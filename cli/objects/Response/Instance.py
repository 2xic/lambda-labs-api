from .Region import Region
from .BaseInstance import BaseInstance

class Instance(BaseInstance):
    def __init__(self, entry) -> None:
        super().__init__(entry["instance_type"])

        regions_with_capacity_available = entry["regions_with_capacity_available"]

        self.regions_with_capacity_available = list(map(Region, regions_with_capacity_available))


    def __str__(self):
        return f"{self.name} ({self.status}) {self.price_dollar}$ per hour"

    @property
    def status(self):
        if self.is_available:
            return "available"
        return "unavailable"

    @property
    def is_available(self):
        return len(self.regions_with_capacity_available)
