#!/usr/bin/env python3

from aws_cdk import (
    core
)

from cdk_lambda.cdk_lambda_stack import CdkLambdaStack
from cdk_apigateway.cdk_api_stack import CdkAPIGatewayStack
from cdk_elasticsearch.cdk_elasticsearch_stack import CdkElasticSearchStack
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
    id    = "cdk-lambda", 
    env   = {
        'region': 'us-east-1',
        'account': '065035205697'
        }
)

functions.auto.grant_invoke(functions.lambdaEdge)
functions.home.grant_invoke(functions.lambdaEdge)

# Creating a Stack for API Gateway:
api = CdkAPIGatewayStack(
    scope = app, 
    id    = "cdk-api", 
    env   = {
        'region': 'us-east-1',
        'account': '065035205697'
    },
    _handler = functions.lambdaEdge
)

# Creating a Stack for Elastic Search:
es = CdkElasticSearchStack(
    scope = app,
    id    = "cdk-elasticSearch",
    env   = {
        'region': 'us-east-1',
        'account': '065035205697'
    }
)


# Adding Tags to Resources:
for tag, value in tags.items():
    core.Tag.add(functions.lambdaEdge, tag, value)
    core.Tag.add(functions.auto, tag, value)
    core.Tag.add(functions.home, tag, value)
    core.Tag.add(api.api, tag, value)

app.synth()
