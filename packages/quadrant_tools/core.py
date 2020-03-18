import elasticache_auto_discovery
from pymemcache.client.hash import HashClient

class Quadrant_Tools:

    def __init__(self):
        pass

    @staticmethod
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

    @staticmethod
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