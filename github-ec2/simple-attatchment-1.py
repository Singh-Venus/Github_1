import boto3
ses = boto3.client('ses')
response = ses.send_raw_email(
    Destinations=[
    ],
    FromArn='your profile ARN',
    RawMessage={
        'Data': 'From: Senders@email.com\nTo: receivers@email.com\nSubject: Test_email '
                'email (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; '
                'boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename="attachment.txt"\n\nThis is the text in the attachment.\n\n--NextPart--',

    },
    ReturnPathArn='',
    Source=' ',
    SourceArn='your Arn',
)

print(response)