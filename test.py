from cli.Lambda import Lambda
from cli.objects.RequestInstance import RequestInstance
from cli.objects.RequestTerminateInstances import RequestTerminateInstances

cli = Lambda()
response = cli.get_offered_instances()
print(response)

instances = filter(lambda x: x.is_available, response)
instances = sorted(instances, key=lambda x: x.price_dollar)

first_instance = instances[0]
request = RequestInstance(
    first_instance.regions_with_capacity_available[0],
    first_instance,
    ssh_keys=["cloud"]
)
print(request)
#cli.launch_instance(
#    request
#)
print(cli.get_running_instances())
cli.stop_instances(
    RequestTerminateInstances([])   
)

cli.stop_all_instances()

