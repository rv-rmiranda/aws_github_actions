from aws_cdk import (
    core,
    aws_lambda,
    aws_apigateway as api
)

class CdkLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.hello = aws_lambda.Function(
            self, "HelloHandler",
            runtime     = aws_lambda.Runtime.PYTHON_3_8,
            code        = aws_lambda.Code.asset('lambda'),
            handler     = "hello.handler",
            memory_size = 1024,
            environment = {
                "PATH": "./"
            }
        )

        self.hello2 = aws_lambda.Function(
            self, "HelloHandler2",
            runtime = aws_lambda.Runtime.PYTHON_3_8,
            code    = aws_lambda.Code.asset('lambda'),
            handler = "hello2.handler",
            memory_size= 1024
        )
