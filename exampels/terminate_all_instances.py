from lambda_cli.cli.Lambda import Lambda
from lambda_cli.cli.objects.Request.RequestTerminateInstances import RequestTerminateInstances

cli = Lambda()
response = cli.get_offered_instances()
cli.stop_all_instances()

