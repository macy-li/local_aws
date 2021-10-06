
#  Builds a serverless application and prepare for deployment or local testing
samlcoal build

#  invoke lambda function locally
samlocal local invoke

# deploy SAM to localstack
samlocal deploy --guided