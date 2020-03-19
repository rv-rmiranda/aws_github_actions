
from aws_cdk import (
    core,
    aws_elasticache as EC
)

import boto3

# === CdkElastiCasheStack ===

class CdkElastiCasheStack(core.Stack):

    '''
    The CdkElastiCasheStack class define the infrastructure of the
    Elasticache-Memcached to be deployed into the AWS accounts.

    **Documentation:**

    https://docs.aws.amazon.com/lambda/latest/dg/services-elasticache-tutorial.html
    https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_elasticache/CfnCacheCluster.html
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engineversion
    '''

    def get_lambda_security_group(self, lambdas_names:list) -> [list]:
        try:
            sg = list()
            client = boto3.client('lambda')

            for name in lambdas_names:
                response = client.get_function_configuration(
                    FunctionName = name
                )

                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    lambda_sg = response['VpcConfig']['SecurityGroupIds']
                    sg.extend(lambda_sg)
            return sg
        except Exception as e:
            raise e


    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # === Elasticache-Memcached ===

        self.lambda_security_group = self.get_lambda_security_group(['queryElasticache-dev', 'storeElasticache-dev'])
        self.sg = ['sg-b18600f8'].extend(self.lambda_security_group)

        self.elasticache = EC.CfnCacheCluster (
            scope                        = self,
            id                           = 'cdk-memcache',
            auto_minor_version_upgrade   = True,
            az_mode                      = 'single-az',
            cache_node_type              = 'cache.t2.micro',
            cluster_name                 = 'cdk-memcache',
            engine                       = 'memcached',
            engine_version               = '1.5.16',
            num_cache_nodes              = 1,
            port                         = 6379,
            preferred_maintenance_window = 'sun:23:00-mon:01:30',
            vpc_security_group_ids       = self.sg,
            cache_subnet_group_name      = 'coxcomm-subnet-group',
        )
