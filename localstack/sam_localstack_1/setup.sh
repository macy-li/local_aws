
#  Builds a serverless application and prepare for deployment or local testing
samlocal build

#  invoke lambda function locally with event passed in
samlocal local invoke -e events/event.json

# deploy SAM to localstack
samlocal deploy --guided
