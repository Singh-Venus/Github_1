import boto3

ses = boto3.client('ses')

response = ses.send_raw_email(
    Source='senders@email.com',
    Destinations=[
        'receivers@email.com',
    ],
    RawMessage={
        'Data': b''
    },
    FromArn='string',
    SourceArn='string',
    ReturnPathArn='string',
    Tags=[
        {
            'Name': 'string',
            'Value': 'string'
        },
    ],
    ConfigurationSetName='string'
)