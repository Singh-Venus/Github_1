import boto3
ec2_client = boto3.client('ec2')
response = ec2_client.monitor_instances(
    InstanceIds=[
        'Instance Id',
    ],

)
print(response)