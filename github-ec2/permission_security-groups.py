import boto3

ec2_client = boto3.client('ec2')

ip_perm = [{
    'IpProtocol': 'tcp',
    'FromPort': 22,
    'ToPort': 22,
    'UserIdGroupPairs': [{
        'GroupId': 'security group Id',
        'UserId': 'your Id'
    }]
}]

response = ec2_client.authorize_security_group_ingress(
    IpPermissions=ip_perm,
    GroupId='security group Id')
print(response)
