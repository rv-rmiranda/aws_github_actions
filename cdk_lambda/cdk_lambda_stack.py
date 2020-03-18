"""
Documentation:
https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
"""

from aws_cdk import (
    core,
    aws_lambda,
    aws_ec2 as ec2
)

class CdkLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.exciting_vpc = ec2.Vpc.from_lookup(
            scope      = self,
            id         = "VPC",
            vpc_id     = "vpc-a14bf1c5",
            is_default = False
        )

        self.lambdaProxy = aws_lambda.Function(
            self, "ProxyHandler",
            runtime     = aws_lambda.Runtime.PYTHON_3_8,
            code        = aws_lambda.Code.asset('./lambda/proxy'),
            handler     = "lambda_proxy.handler",
            timeout     = core.Duration.seconds(900),
            memory_size = 1024
        )

        self.queryElasticache = aws_lambda.Function(
            self, "QueryElasticacheHandler",
            runtime         = aws_lambda.Runtime.PYTHON_3_8,
            code            = aws_lambda.Code.asset('./lambda/queryElasticach/'),
            handler         = "queryElasticache.handler",
            timeout         = core.Duration.seconds(900),
            memory_size     = 1024,
            vpc             = self.exciting_vpc
        )

        self.storeElasticache = aws_lambda.Function(
            self, "StoreElasticacheHandler",
            runtime         = aws_lambda.Runtime.PYTHON_3_8,
            code            = aws_lambda.Code.asset('./lambda/storeElasticache'),
            handler         = "storeElasticache.handler",
            timeout         = core.Duration.seconds(900),
            memory_size     = 1024,
            vpc             = self.exciting_vpc
        )

        self.queryQuadrant = aws_lambda.Function(
            self, "QuadrantHandler",
            runtime         = aws_lambda.Runtime.PYTHON_3_8,
            code            = aws_lambda.Code.asset('./lambda/queryQuadrant'),
            handler         = "queryQuadrant.handler",
            timeout         = core.Duration.seconds(900),
            memory_size     = 1024,
            vpc             = self.exciting_vpc
        )
