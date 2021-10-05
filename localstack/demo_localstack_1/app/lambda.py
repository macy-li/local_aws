import boto3
import json
import os

if os.getenv( 'LOCALSTACK' , "").lower() == 'true':

    s3 = boto3.resource( 's3', endpoint_url = "http://host.docker.internal:4566/" )

else:

    s3 = boto3.resource( 's3' )


def lambda_handler( event, context ):
    out = None
    try:
        s3_bucket = 'macy-localstack-demo'

        for record in event[ 'Records' ]:
            body = json.loads( record[ "body" ] )

            key = body[ 'filename' ]
            val = body[ 'value' ]

            value = sum( list( val ) )

            file_name = '%s.txt' % key

            obj = s3.Object( s3_bucket, file_name )

            obj.put( Body = b'%d' % value )

            out = (key, value)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        print( e )
        # throw exception, do not handle. Lambda will make message visible again.
        raise e

    return out
