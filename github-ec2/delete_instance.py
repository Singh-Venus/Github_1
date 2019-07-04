import boto3

ec2_client = boto3.client('ec2', region_name='your region name', aws_access_key_id='your access key Id',
                          aws_secret_access_key='your access key')
response = ec2_client.terminate_instances(
    InstanceIds=[
        'Your Instance Id',
    ],
)
print(response)
