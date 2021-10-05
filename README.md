# local_aws
Contains sample code to develop and test AWS applications locally.
    .
    ├── localstack              # Test files (alternatively `spec` or `tests`)
    │   ├── sam_localstack      # SAM to deploy lambda in localstack
    │   ├── sam_localstack_1    # SAM to deploy lambda in localstack ( SQS as event source )
    │   └── lambda              # test lambda function with localstack 
    ├── moto                    # test cases with moto
    └── Readme.md

## localstack
localstack is a cloud service emulator that runs in a single container on your laptop or in your CI environment.

### Requirements

* `python` (Python 3.6 up to 3.9 supported)
* `pip` (Python package manager)
* `Docker`

### Install

The easiest way to install LocalStack is via `pip`:
```
pip install localstack
```

#### Localstack AWS CLI (optional)
The project provides the awslocal command line, a simple wrapper around the `aws` command line interface for use with LocalStack.
```
pip install awscli-local
```

#### Localstack AWS SAM CLI 
The project provides the samlocal command line, a simple wrapper around the `aws sam` CLI for use with LocalStack.

```
pip install aws-sam-cli-local
```

### Running

By default, LocalStack is started inside a Docker container by running:
```
localstack start
```

### For more information please refer to [loclstack github repo](https://github.com/localstack/localstack)


## Moto
Moto is a library that allows your tests to easily mock out AWS services.

## Install

To install moto for a specific service:
```console
$ pip install moto[ec2,s3]
```
This will install Moto, and the dependencies required for that specific service.  
If you don't care about the number of dependencies, or if you want to mock many AWS services:
```console
$ pip install moto[all]
```

### For more information please refer to [moto github repo](https://github.com/spulec/moto)







