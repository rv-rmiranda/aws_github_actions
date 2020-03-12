#!/usr/bin/env python3

from aws_cdk import (
    core
)

from cdk_lambda.cdk_lambda_stack import CdkLambdaStack
from cdk_apigateway.cdk_api_stack import CdkAPIGatewayStack

# Tagging resources
# See https://github.com/RedVentures/cnn/blob/master/0001-tagging-aws-resources.md
tags = {'AssetTag': 'n/a',
        'Backup': 'n/a',
        'Classification': 'n/a',
        'Environment': 'test',
        'Expiration': 'n/a',
        'Name': 'Forward787 CDK Test',
        'Owner': 'Sancocho Team',
        'Partner': 'n/a',
        'Project': 'rv-forward787',
        'Provisioner': 'AWS CDK',
        'Service': 'Provision architecture for licensing tool thru AWS cdk.',
        'Version': 'n/a'
        }

app = core.App()

# Creating a Stack for Lambdas:
functions = CdkLambdaStack(
    scope = app, 
    id    = "cdk-test", 
    env   = {
        'region': 'us-east-1',
        'account': 'ID'
        }
)

# Creating a Stack API Gateway:
api = CdkAPIGatewayStack(
    scope = app, 
    id    = "cdk-api", 
    env   = {
        'region': 'us-east-1',
        'account': 'ID'
        },
    _handler = functions.hello
)


# Adding Tags to Resources:
for tag, value in tags.items():
    core.Tag.add(functions.hello, tag, value)
    core.Tag.add(functions.hello2, tag, value)
    core.Tag.add(api.api, tag, value)

app.synth()
