from .Requester import Requester
from .objects.Response.Instance import Instance
from .objects.Request.RequestInstance import RequestInstance
from .objects.Response.NewInstance import NewInstance
from .objects.Response.TerminatedInstances import TerminatedInstances
from .objects.Response.RunningInstance import RunningInstance
from .objects.Request.RequestTerminateInstances import RequestTerminateInstances
from .Database import Database
from typing import List

class Lambda:
    def __init__(self) -> None:
        self.requester = Requester()
        self.database = Database()

    def get_offered_instances(self) -> List[Instance]:
        json = self.requester.get(
            "instance-types"
        )
        return list(map(Instance, json["data"].values()))
    
    def get_running_instances(self) -> List[RunningInstance]:
        json = self.requester.get(
            "instances"
        )
        running_instances = list(map(RunningInstance, json["data"]))
        self.database.add_instance(running_instances)

        return running_instances

    def launch_instance(self, request: RequestInstance):
        json = self.requester.post(
            "instance-operations/launch",
            request.payload()
        )
        new_instances = list(map(NewInstance, json['data']['instance_ids']))
        self.database.add_instance(new_instances)
        return new_instances

    def stop_instances(self, request: RequestTerminateInstances):
        json = self.requester.post(
            "instance-operations/terminate",
            request.payload()
        )
        return list(map(TerminatedInstances, json["data"]['terminated_instances']))

    # stops the instances tracked by the cli
    def stop_all_instances(self):
        ids = self.database.read()
        self.database.remove_instance(self.stop_instances(RequestTerminateInstances(ids)))
