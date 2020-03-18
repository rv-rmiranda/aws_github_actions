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
        print("Getting Elasticache Config")
        elasticache_config_endpoint = memcached_endpoint
        print("Getting Elasticache Nodes")
        nodes = elasticache_auto_discovery.discover(elasticache_config_endpoint)
        nodes = map(lambda x: (x[1], int(x[2])), nodes)
        
        return HashClient(nodes)

    except Exception as e:
        raise e

def handler(event, context):
    """
    This function gets data from memcache.
    Memcache is hosted using elasticache
    """

    try:
        # Set Memcached Client:
        memcache_client = set_elasticache_client('cdk-memcache.ygxeqs.cfg.use1.cache.amazonaws.com:6379')
        
        # Converting input Dictionario into a JSON string... this will be the sample element we add to the cache.
        hashKey = event['hashKey']

        # Get data from cache.
        cached_data = memcache_client.get(hashKey)

        if cached_data:
            return http_responce(200, cached_data)
        else:
            return http_responce(400, "")

    except Exception as e:
        return http_responce(400, str(e))
        