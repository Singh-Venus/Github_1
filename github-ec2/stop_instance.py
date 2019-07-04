import boto3
ec2_client = boto3.client('ec2',region_name='your region', aws_access_key_id='your access key Id', aws_secret_access_key='your secret access key')
response = ec2_client.stop_instances(
    InstanceIds=[
        'Instance Id',
    ],
    )
print(response)