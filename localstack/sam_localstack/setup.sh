
#  Builds a serverless application and prepare for deployment or local testing
PIP_CONFIG_FILE=pip.conf samlcoal build

#  invoke lambda function locally
samlocal local invoke

# deploy SAM to localstack
samlocal deploy --guided
