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

def test_lambda_queryElasticache_created():
    assert("queryElasticache.handler" in get_template())

def test_lambda_storeElasticache_created():
    assert("storeElasticache.handler" in get_template())

def test_lambda_lambda_proxy_created():
    assert("lambda_proxy.handler" in get_template())

def test_lambda_queryQuadrant_created():
    assert("queryQuadrant.handler" in get_template())
