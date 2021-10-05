import boto3
import json
import os

s3_bucket = 'macy-localstack-demo'

if os.getenv( 'LOCALSTACK' , "").lower() == 'true':

    queue_url = 'http://host.docker.internal:4566/000000000000/my-queue'
    s3 = boto3.resource( 's3', endpoint_url = "http://host.docker.internal:4566/" )
    sqs = boto3.client( 'sqs', endpoint_url = "http://host.docker.internal:4566/", use_ssl = False )


else:
    queue_url = 'https://sqs.ap-southeast-2.amazonaws.com/623252393094/my-queue'
    s3 = boto3.resource( 's3' )
    sqs = boto3.client( 'sqs', use_ssl = False )


def lambda_handler( event, context ):
    response = sqs.receive_message(
        QueueUrl = queue_url,
        AttributeNames = [
            'SentTimestamp'
        ],
        MaxNumberOfMessages = 7,
        MessageAttributeNames = [
            'All'
        ],
        VisibilityTimeout = 10,
        WaitTimeSeconds = 0
    )

    out = None

    for each_msg in response.get( "Messages", [ ] ):

        body = json.loads(each_msg['Body'].replace("'", "\""))

        key = body[ 'filename' ]

        val = body[ 'value' ]

        value = sum( list( val ) )

        file_name = '%s.txt' % key

        obj = s3.Object( s3_bucket, file_name )

        obj.put( Body = b'%d' % value )

        out = (key, value)

        receipt_handle = each_msg[ 'ReceiptHandle' ]
        sqs.delete_message(
            QueueUrl = queue_url,
            ReceiptHandle = receipt_handle
        )

    return out
