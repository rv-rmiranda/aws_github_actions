"""
Documentation:
https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_elasticsearch/CfnDomain.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-vpcoptions
https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-dedicatedmasternodes.html
"""

from aws_cdk import (
    core,
    aws_elasticsearch as ES
)

class CdkElasticSearchStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.elasticSearch = ES.CfnDomain(
            self,
            "CDKElasticSearch",
            domain_name           = "cdk-elasticsearch",
            elasticsearch_version = "7.4",
            access_policies = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": [
                        "*"
                        ]
                    },
                    "Action": [
                        "es:*"
                    ],
                    "Resource": "arn:aws:es:us-east-1:065035205697:domain/cdk-test/*"
                    }
                ]
            },
            elasticsearch_cluster_config = ES.CfnDomain.ElasticsearchClusterConfigProperty(
                dedicated_master_enabled = True, # NOTE: Change to True in Production
                dedicated_master_count   = 3, # Even numbers of dedicated masters are not recommended.
                dedicated_master_type    = "t2.small.elasticsearch",
                instance_count           = 1,
                instance_type            = "t2.small.elasticsearch",
                zone_awareness_enabled   = False
            ),
            vpc_options = ES.CfnDomain.VPCOptionsProperty(
                security_group_ids = ["sg-e0fea685"],
                subnet_ids         = ["subnet-01e89264"]
            ),
            ebs_options = ES.CfnDomain.EBSOptionsProperty(
                ebs_enabled = True,
                iops        = 0,
                volume_size = 20,
                volume_type = "gp2"
            ),
            snapshot_options = ES.CfnDomain.SnapshotOptionsProperty (
                automated_snapshot_start_hour = 0
            ),
            cognito_options= ES.CfnDomain.CognitoOptionsProperty(
                enabled = False
            )
        )