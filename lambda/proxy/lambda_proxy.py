import json
import boto3

#  Move 
def http_responce(status:int=400, body:str=""):
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

def generate_hash(*args):
    pass

# Local Functions:
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

def get_quadrant_data(params):
    pass

def get_cached_data(hash_key:str, params):
    try:
        responce =  invoke_lambda(
            arn  = "arn:aws:lambda:us-east-1:960785399995:function:cdk-lambda-QueryElasticacheHandler3C0A3A45-1WCZ7HO0ET6G0",
            data = params
        )

        return http_responce(200, json.dumps(responce))
    except Exception as e:
        return http_responce(400, json.dumps(e))

def store_data_in_cache(hash_key:str, params):
    try:
        responce =  invoke_lambda(
            arn  = "arn:aws:lambda:us-east-1:960785399995:function:cdk-lambda-StoreElasticacheHandler5E55085E-1VUXINE283NBI",
            data = params
        )

        return http_responce(200, json.dumps(responce))
    except Exception as e:
        return http_responce(400, json.dumps(e))

def handler(event, context):
    
    try:

        # Lambda Logs: 
        print(event)

        path = event['pathParameters']['proxy']
        params = event['queryStringParameters']

        # TODO - Manage HTTP Request Routing 

        if path == 'auto':
            # TODO - Data Format
            hash_hey = generate_hash()
            response = get_cached_data(hash_hey, params)

            if response['statusCode'] == 200:
                # TODO - Data Format
                return response
            else:
                response = get_quadrant_data(params)
                if response['statusCode'] == 200:
                    # TODO - Data Format
                    return response
                
            return response
        elif path == 'home':
            
            # TODO - Data Format
            hash_hey = generate_hash()
            response = get_cached_data(hash_hey, params)

            if response['statusCode'] == 200:
                # TODO - Data Format
                return response
            else:
                response = get_quadrant_data(params)
                if response['statusCode'] == 200:
                    # TODO - Data Format
                    return response

        else:
            body = "ERROR: Path {0} not supported".format(path)
            return http_responce(body=body)

    except Exception as e:
        http_responce(body=str(e))