import json
import pytest

from aws_cdk import core
from cdk_lambda.cdk_lambda_stack import CdkLambdaStack


def get_template():
    app = core.App()
    CdkLambdaStack(app, "cdk-lambda")
    return json.dumps(app.synth().get_stack("cdk-lambda").template)


def test_lambda_created():
    assert("AWS::Lambda::Function" in get_template())

def test_lambda_edge_created():
    assert("lambda_edge.handler" in get_template())

def test_lambda_auto_created():
    assert("auto.handler" in get_template())

def test_lambda_home_created():
    assert("home.handler" in get_template())
