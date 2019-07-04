import boto3
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(

    GroupIds=[
        'your security-group Id',
    ],
    GroupNames=[
        'security group name',
    ],
)
print(response)