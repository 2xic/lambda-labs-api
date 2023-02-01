from lambda_cli.cli.Lambda import Lambda
from lambda_cli.cli.objects.Request.RequestInstance import RequestInstance

cli = Lambda()

print(cli.get_running_instances())
