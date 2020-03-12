import json
import boto3

def http_responce(status:int, body:str):
    try:
        return {
            'statusCode': status,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': body
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': str(e)
        }

def get_response(response):
    payload = json.loads(response.get('Payload').read())

    return {
        "statusCode": payload['statusCode'],
        "body": payload['body']
    }

def invoke_lambda(arn:str, data:dict):
    try:
        client = boto3.client('lambda')
        response = client.invoke(
            FunctionName=arn,
            InvocationType='RequestResponse',
            Payload=json.dumps(data)
        )

        payload = get_response(response)

        if payload['statusCode'] == 200:
            return payload['body']
        else:
            raise Exception(payload['body'])

    except Exception as e:
        raise e

def handler(event, context):
    
    try:

        # Lambda Logs: 
        print(event)

        path = event['pathParameters']['proxy']
        params = event['queryStringParameters']

        if path == 'auto':

            responce =  invoke_lambda(
                arn  = "arn:aws:lambda:us-east-1:065035205697:function:cdk-lambda-AutoHandler276EDDAB-8GGZ0PL4I7RV",
                data = params
            )

            return http_responce(200, json.dumps(responce))

        elif path == 'home':

            responce = invoke_lambda(
                arn  = "arn:aws:lambda:us-east-1:065035205697:function:cdk-lambda-HomeHandler01436A24-63AOO9JVK4CE",
                data = params
            )

            return http_responce(200, json.dumps(responce))

        else:
            body = "ERROR: Path {0} not supported".format(path)
            http_responce(400, body)


    
    except Exception as e:
        http_responce(400, str(e))