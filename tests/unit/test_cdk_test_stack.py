import json
import pytest

from aws_cdk import core
from cdk_lambda.cdk_lambda_stack import CdkLambdaStack


def get_template():
    app = core.App()
    CdkLambdaStack(app, "cdk-test")
    return json.dumps(app.synth().get_stack("cdk-test").template)


def test_lambda_created():
    assert("AWS::Lambda::Function" in get_template())

def test_lambda_hello_created():
    assert("hello.handler" in get_template())

def test_lambda_hello2_created():
    assert("hello2.handler" in get_template())
