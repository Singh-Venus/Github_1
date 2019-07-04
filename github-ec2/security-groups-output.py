import boto3
ec2client = boto3.client('ec2')
response = ec2client.describe_security_groups()
for reservation in response["Reservations"]:
    for security_groups in reservation["SecurityGroups"]:
        print(security_groups)

        print(security_groups["SecurityGroupIds"])