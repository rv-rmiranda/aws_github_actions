import json
import time
import uuid
import sys
import socket
import elasticache_auto_discovery
from pymemcache.client.hash import HashClient

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

def set_elasticache_client(memcached_endpoint:str):
    try:
        print('Getting Elasticache Config')
        elasticache_config_endpoint = memcached_endpoint
        print('Getting Elasticache Nodes')
        nodes = elasticache_auto_discovery.discover(elasticache_config_endpoint)
        nodes = map(lambda x: (x[1], int(x[2])), nodes)
        
        return HashClient(nodes)

    except Exception as e:
        raise e

def handler(event, context):
    """
    This function puts data into memcache.
    Memcache is hosted using elasticache
    """

    try:
        # Set Memcached Client:
        memcache_client = set_elasticache_client('cdk-memcache.ygxeqs.cfg.use1.cache.amazonaws.com:6379')

        # HashKey:
        hashKey = event['hashKey']
        
        # Converting input Dictionario into a JSON string. This is the data element added to the cache:
        data_inserted = json.dumps(event['data'])

        # Storeing data into cache:
        response = memcache_client.set('json', data_inserted)
        print(response)

        body = json.dumps({
            'hashKey': hashKey
        })

        return http_responce(200, body)

    except Exception as e:
        return http_responce(400, str(e))