from .Region import Region
from .Instance import Instance

class RequestInstance:
    def __init__(
        self,
        region: Region,
        instance: Instance,
        ssh_keys=[],
        file_system_names=[],
        quantity=1
    ):
        self.region_name = region.name
        self.instance_name = instance.name
        self.ssh_keys = ssh_keys
        self.file_system_names = file_system_names
        self.quantity = quantity

    def payload(self):
        return {
            "region_name": self.region_name,
            "instance_type_name": self.instance_name,
            "ssh_key_names": self.ssh_keys,
            "file_system_names": self.file_system_names,
            "quantity": self.quantity
        }
