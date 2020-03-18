"""
Documentation:
https://docs.aws.amazon.com/lambda/latest/dg/services-elasticache-tutorial.html
https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_elasticache/CfnCacheCluster.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engineversion
"""

from aws_cdk import (
    core,
    aws_elasticache as EC
)

class CdkElastiCasheStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.elasticache = EC.CfnCacheCluster (
            scope                        = self,
            id                           = "cdk-memcache",
            auto_minor_version_upgrade   = True,
            az_mode                      = "single-az",
            cache_node_type              = "cache.t2.micro",
            cluster_name                 = "cdk-memcache",
            engine                       = "memcached",
            engine_version               = "1.5.16",
            num_cache_nodes              = 1,
            port                         = 6379,
            preferred_maintenance_window = "sun:23:00-mon:01:30",
            vpc_security_group_ids       = ["sg-b18600f8","sg-0f19fdd00964ed093", "sg-03461af57009b0d8d"],
            cache_subnet_group_name      = "coxcomm-subnet-group",
        )