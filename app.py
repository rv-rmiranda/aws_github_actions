#!/usr/bin/env python3\

"""
Documentation:
CDK:
    - https://docs.aws.amazon.com/cdk/api/latest/python/modules.html
Tagging resources
    — https://github.com/RedVentures/cnn/blob/master/0001-tagging-aws-resources.md
"""
import os
from aws_cdk import (
    core,
    aws_lambda as lam
)

from cdk_lambda.cdk_lambda_stack import CdkLambdaStack
from cdk_apigateway.cdk_api_stack import CdkAPIGatewayStack
from cdk_elasticsearch.cdk_elasticsearch_stack import CdkElasticSearchStack
from cdk_elasticache.cdk_elasticache_stack import CdkElastiCasheStack

tags = {
    'AssetTag': 'n/a',
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
__env = {
    'region': os.environ['CDK_DEFAULT_REGION'],
    'account': os.environ['CDK_DEFAULT_ACCOUNT']
}
# __stage = os.environ['STAGE']

# Creating a Stack for Lambdas:
functions = CdkLambdaStack(
    scope = app, 
    id    = "cdk-lambda", 
    env   = __env,
)

# Creating a Stack for API Gateway:
api = CdkAPIGatewayStack(
    scope = app, 
    id    = "cdk-api", 
    env   = __env,
    _handler = functions.lambdaProxy
)

ec = CdkElastiCasheStack (
    scope = app,
    id    = "cdk-memcached",
    env   = __env
)


# Granting Permissions:
functions.queryElasticache.grant_invoke(functions.lambdaProxy)
functions.storeElasticache.grant_invoke(functions.lambdaProxy)
functions.queryQuadrant.grant_invoke(functions.lambdaProxy)

# Adding Tags to Resources:
for tag, value in tags.items():
    core.Tag.add(functions.lambdaProxy, tag, value)
    core.Tag.add(functions.queryQuadrant, tag, value)
    core.Tag.add(functions.queryElasticache, tag, value)
    core.Tag.add(functions.storeElasticache, tag, value)
    core.Tag.add(api.api, tag, value)
    core.Tag.add(ec.elasticache, tag, value)

app.synth()
