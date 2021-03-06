import os
from pathlib import Path

from constructs import Construct

from aws_cdk import App, Environment, Stack, Duration
from aws_cdk import aws_apigateway, aws_lambda
from aws_cdk.aws_lambda_python_alpha import PythonFunction

SRC = Path(__file__).parent.parent / "backend" / "src"


class FastApiService(Construct):
    def __init__(self, scope: Construct, id_: str):
        super().__init__(scope, id_)

        handler = PythonFunction(
            self,
            "BackendHandler",
            entry=str(SRC.as_posix()),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            index='lambda.py',
            handler="handler",
            timeout=Duration.seconds(30)
        )

        api = aws_apigateway.LambdaRestApi(
            self,
            "BackendApiGateWay",
            handler=handler,
            rest_api_name="Disaster Recovery",
            description="A Simple Disaster Recovery API",
            proxy=True,
            default_cors_preflight_options=aws_apigateway.CorsOptions(
                allow_methods=['GET', 'POST', 'PUT', 'OPTIONS'],
                allow_origins=[
                    "http://localhost:3000",
                    "https://imokay.tech",
                    "https://www.imokay.tech"
                ]
            )
        )


class BackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        FastApiService(self, "FastAPI")


app = App()
BackendStack(app, "DisasterStack", env=Environment(account="591968328369", region="us-east-1"))
app.synth()
