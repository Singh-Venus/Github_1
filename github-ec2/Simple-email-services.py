import boto3
client = boto3.client(
    'ses',
    region_name='your region',
    aws_access_key_id='your access key id',
    aws_secret_access_key='your access key')

response = client.send_email(
    Destination={
        'ToAddresses': [
            'receivers email',
                    ],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is first email generation using python boto3.',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test_Email using python Boto 3',
        },
    },
    Source='senders email',
)