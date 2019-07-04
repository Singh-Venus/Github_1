import boto3
ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description='give a description',
    GroupName='your security group name',
    VpcId='your vpc Id',

)