from lambda_cli.cli.Lambda import Lambda
from lambda_cli.cli.objects.Request.RequestInstance import RequestInstance

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

print(cli.launch_instance(
    request
))
