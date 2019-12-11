import boto3
import os

ec2 = boto3.resource('ec2')
client = boto3.client('elb')

def lambda_handler(event, context):
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for instance in instances:
        response = client.register_instances_with_load_balancer(
            LoadBalancerName='VaporLB',
            Instances=[
                {
                'InstanceId': instance.id
                },
            ]
        )
        print(instance.id)