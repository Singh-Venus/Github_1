import boto3
import re

ec2_client = boto3.client('ec2')
responce = ec2_client.describe_instances(InstanceIds=['Instance Id'])
if responce:
    status = responce['Reservations'][0]['Instances'][0]
    if status['State']['Name'] == 'stopped':
        stopped_reason = status['StateTransitionReason']
        current_time = responce['ResponseMetadata']['HTTPHeaders']['date']
        stopped_time = re.findall('.*\((.*)\)', stopped_reason)[0]
        print('Stopped time:', stopped_time)
        print('Current time:', current_time)
