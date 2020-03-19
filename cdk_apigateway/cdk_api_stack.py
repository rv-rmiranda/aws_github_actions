from aws_cdk import (
    core,
    aws_apigateway as api
)

# === CdkAPIGatewayStack ===
class CdkAPIGatewayStack(core.Stack):

    """
    The CdkAPIGatewayStack class define the infrastructure of the
    API Gateway to be deployed into the AWS accounts.

    **Documentation:**

    https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/LambdaRestApi.html
    """

    def __init__(self, scope: core.Construct, id: str, _handler, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # === API Gateway ===

        self.api = api.LambdaRestApi(
            scope         = self, 
            id            = "cdk-api",
            handler       = _handler,
            proxy         = True,
            rest_api_name = "CDK-API-Test"
        )