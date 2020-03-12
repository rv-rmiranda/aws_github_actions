from aws_cdk import (
    core,
    aws_lambda,

)

class CdkLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.lambdaEdge = aws_lambda.Function(
            self, "EdgeHandler",
            runtime     = aws_lambda.Runtime.PYTHON_3_8,
            code        = aws_lambda.Code.asset('lambda'),
            handler     = "lambda_edge.handler",
            timeout     = core.Duration.seconds(900),
            memory_size = 1024,
            environment = {
                "PATH": "./"
            }
        )

        self.auto = aws_lambda.Function(
            self, "AutoHandler",
            runtime    = aws_lambda.Runtime.PYTHON_3_8,
            code       = aws_lambda.Code.asset('lambda'),
            handler    = "auto.handler",
            timeout    = core.Duration.seconds(900),
            memory_size = 1024
        )

        self.home = aws_lambda.Function(
            self, "HomeHandler",
            runtime     = aws_lambda.Runtime.PYTHON_3_8,
            code        = aws_lambda.Code.asset('lambda'),
            handler     = "home.handler",
            timeout     = core.Duration.seconds(900),
            memory_size = 1024
        )
