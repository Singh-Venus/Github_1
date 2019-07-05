import boto3

client = boto3.client('ec2',region_name='your region', aws_access_key_id='your access key id', aws_secret_access_key='your access key')
response = client.create_vpc(

    CidrBlock='string',
    AmazonProvidedIpv6CidrBlock=True|False,
    DryRun=True|False,
    InstanceTenancy='default'|'dedicated'|'host'
)

print(response)