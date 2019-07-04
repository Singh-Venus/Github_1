import boto3

ec2 = boto3.client('ec2', region_name='your region', aws_access_key_id='your access key id', aws_secret_access_key='your access key')

response = ec2.delete_key_pair(
    KeyName='your-key',
   )
print(response)