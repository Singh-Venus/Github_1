import boto3
ec2_client = boto3.client('ec2')

response = ec2_client.import_key_pair(
    KeyName='string',
    PublicKeyMaterial=b'bytes'

)