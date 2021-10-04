import unittest

import boto3
from moto import mock_s3


def test_upload( bucket_name, key, content ):
    s3 = boto3.resource( 's3' )
    object = s3.Object( bucket_name, key )
    object.put( Body = content )


class TestS3( unittest.TestCase ):
    mock_s3 = mock_s3()
    bucket_name = 'test-bucket'

    def setUp( self ):
        self.mock_s3.start()

        s3 = boto3.resource( 's3' )
        bucket = s3.Bucket( self.bucket_name )
        bucket.create(
            CreateBucketConfiguration = {
                'LocationConstraint': 'af-south-1'
            } )

    def tearDown( self ):
        self.mock_s3.stop()

    def test( self ):
        content = b"abc"
        key = '/path/to/obj'

        # run the file which uploads to S3
        test_upload( self.bucket_name, key, content )

        # check the file was uploaded as expected
        s3 = boto3.resource( 's3' )
        object = s3.Object( self.bucket_name, key )
        actual = object.get()[ 'Body' ].read()

        self.assertEqual( actual, content )


if __name__ == '__main__':
    unittest.main()
