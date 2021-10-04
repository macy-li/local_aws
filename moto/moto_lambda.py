import io
import json
import unittest
import zipfile

import boto3
from moto import mock_lambda, mock_iam

_lambda_region = 'ap-southeast-2'

def get_role_name():
    with mock_iam():
        iam = boto3.client( "iam", region_name = _lambda_region )
        return iam.create_role(
            RoleName = "my-role",
            AssumeRolePolicyDocument = "some policy",
            Path = "/my-path/",
        )[ "Role" ][ "Arn" ]


def _process_lambda( func_str ):
    zip_output = io.BytesIO()
    zip_file = zipfile.ZipFile( zip_output, "w", zipfile.ZIP_DEFLATED )
    zip_file.writestr( "lambda_function.py", func_str )
    zip_file.close()
    zip_output.seek( 0 )
    return zip_output.read()


def get_test_zip_file1():
    pfunc = """
def lambda_handler(event, context):
    return event
"""
    return _process_lambda( pfunc )


class MyLambda( unittest.TestCase ):
    mock_lambda = mock_lambda()

    def setUp( self ):
        self.mock_lambda.start()
        conn = boto3.client( 'lambda', _lambda_region )
        conn.create_function(
            FunctionName = 'lambda-function-name',
            Runtime = 'python3.8',
            Role = get_role_name(),
            Handler = 'lambda_function.lambda_handler',
            Code = {
                'ZipFile': get_test_zip_file1(),
            },
            Description = 'test lambda function',
            Timeout = 3,
            MemorySize = 128,
            Publish = True
        )

    def tearDown( self ):
        self.mock_lambda.stop()

    def test_invoke( self ):
        conn = boto3.client( 'lambda', _lambda_region )
        request = { 'message': 'Hello World!' }

        lambda_response = conn.invoke(
            FunctionName = 'lambda-function-name',
            InvocationType = 'RequestResponse',
            Payload = json.dumps( request )
        )

        response = lambda_response[ 'Payload' ].read()
        response = json.loads( response )
        print( response )

        self.assertEqual( response[ 'message' ], 'Hello World!' )


if __name__ == '__main__':
    unittest.main()
