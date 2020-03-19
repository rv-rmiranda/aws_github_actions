import json
import pytest

from aws_cdk import core
from cdk_lambda.cdk_lambda_stack import CdkLambdaStack
from cdk_apigateway.cdk_api_stack import CdkAPIGatewayStack

def get_template():
    app = core.App()
    func = CdkLambdaStack(app, "cdk-lambda")
    CdkAPIGatewayStack(app, "cdk-api", _handler=func.lambdaProxy)

    api_template = app.synth().get_stack("cdk-api").template

    return json.dumps(api_template)

def test_lambda_api_created():
    assert("AWS::ApiGateway::RestApi" in get_template())