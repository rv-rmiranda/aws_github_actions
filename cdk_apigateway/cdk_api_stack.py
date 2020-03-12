from aws_cdk import (
    core,
    aws_apigateway as api
)

class CdkAPIGatewayStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, _handler, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.api = api.LambdaRestApi(self, "cdk-api",
            handler = _handler,
            proxy   = True,
            rest_api_name = "CDK-API-Test"
        )