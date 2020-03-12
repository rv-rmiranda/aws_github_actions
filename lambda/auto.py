import json

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

def handler(event, context):
    try:
        return http_responce(200, 'Hello Auto!')
    except Exception as e:
        return http_responce(400, str(e))
        