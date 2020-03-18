import os
from aws_cdk import (
    core,
    aws_lambda,
    aws_ec2 as ec2
)

# === CdkLambdaStack ===
class CdkLambdaStack(core.Stack):

    """
    The CdkLambdaStack class define the infrastructure of the Lambda functions
    to be deployed into the AWS accounts.

    **Documentation:**

    https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
    """

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # === VPC ===

        """
        We importing the excising VPC vpc-a14bf1c5.
        """
        self.exciting_vpc = ec2.Vpc.from_lookup(
            scope      = self,
            id         = 'VPC',
            vpc_id     = 'vpc-a14bf1c5',
            is_default = False
        )

        # === Lambda Function Query Elasticache ===
        self.queryElasticache = aws_lambda.Function(
            scope         = self,
            id            = 'QueryElasticacheHandler',
            runtime       = aws_lambda.Runtime.PYTHON_3_8,
            code          = aws_lambda.Code.asset('./lambda/queryElasticach/'),
            handler       = 'queryElasticache.handler',
            timeout       = core.Duration.seconds(900),
            memory_size   = 1024,
            vpc           = self.exciting_vpc,
            function_name = 'queryElasticache-{0}'.format('dev')
        )

        # === Lambda Function Store Elasticache ===
        self.storeElasticache = aws_lambda.Function(
            scope         = self,
            id            = 'StoreElasticacheHandler',
            runtime       = aws_lambda.Runtime.PYTHON_3_8,
            code          = aws_lambda.Code.asset('./lambda/storeElasticache'),
            handler       = 'storeElasticache.handler',
            timeout       = core.Duration.seconds(900),
            memory_size   = 1024,
            vpc           = self.exciting_vpc,
            function_name = 'storeElasticache-{0}'.format('dev')
        )

        # === Lambda Function Proxy ===
        self.lambdaProxy = aws_lambda.Function(
            scope         = self,
            id            = 'ProxyHandler',
            runtime       = aws_lambda.Runtime.PYTHON_3_8,
            code          = aws_lambda.Code.asset('./lambda/proxy'),
            handler       = 'lambda_proxy.handler',
            timeout       = core.Duration.seconds(900),
            memory_size   = 1024,
            function_name = 'lambda_proxy-{0}'.format('dev'),
            environment   = {
                'queryElasticacheARN': core.Stack.format_arn(
                    self,
                    service       = 'lambda',
                    resource      = 'function',
                    sep           = ':',
                    resource_name = self.queryElasticache.function_name
                ),
                'storeElasticacheARN': core.Stack.format_arn(
                    self,
                    service       = 'lambda',
                    resource      = 'function',
                    sep           = ':',
                    resource_name = self.storeElasticache.function_name
                )
            }
        )

        # === Lambda Function Query Quadrant ===
        self.queryQuadrant = aws_lambda.Function(
            scope         = self,
            id            = 'QuadrantHandler',
            runtime       = aws_lambda.Runtime.PYTHON_3_8,
            code          = aws_lambda.Code.asset('./lambda/queryQuadrant'),
            handler       = 'queryQuadrant.handler',
            timeout       = core.Duration.seconds(900),
            memory_size   = 1024,
            vpc           = self.exciting_vpc,
            function_name = 'queryQuadrant-{0}'.format('dev')
        )
