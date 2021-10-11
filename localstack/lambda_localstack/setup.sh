# aws command to create resource in localstack

# create bucket
aws s3 mb s3://macy-localstack-demo --endpoint-url=http://localhost:4566

# create sqs queue  in localstack
aws sqs create-queue --queue-name my-queue --endpoint-url=http://localhost:4566

# send message to queue
aws sqs send-message --queue-url=http://localhost:4566/000000000000/my-queue \
--message-body  '{"filename": "file1" , "value" :[2 ,3, 4] }'  --endpoint-url=http://localhost:4566

# create lambda function
zip function.zip lambda.py

aws lambda create-function --function-name test_lambda --runtime python3.7 \
--role arn:aws:iam::000000000000:role/ \
--zip-file=fileb://function.zip --handler lambda.lambda_handler  --endpoint-url=http://localhost:4566 \
--environment Variables="{LOCALSTACK=True}" --region ap-southeast-2

# invoke lambda function
aws lambda invoke --function-name arn:aws:lambda:ap-southeast-2:000000000000:function:test_lambda \
 --endpoint-url=http://localhost:4566  response.json

# check if file is uploaded to S3
aws s3 ls s3://macy-localstack-demo --endpoint-url=http://localhost:4566



aws lambda create-function --function-name test_lambda3 --runtime python3.8 \
--role arn:aws:iam::000000000000:role/service-role/demoLambda-role-4y0nwuvw \
--zip-file=fileb://function.zip --handler lambda.lambda_handler  --endpoint-url=http://localhost:4566 \
--environment Variables="{LOCALSTACK=True}"
